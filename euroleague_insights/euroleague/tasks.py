import logging

from celery import shared_task

from euroleague_insights.euroleague.euroleague_api.api import EuroleagueAPI
from euroleague_insights.euroleague.euroleague_api.constants import PlayType
from euroleague_insights.euroleague.euroleague_api.constants import Quarter
from euroleague_insights.euroleague.models import Club
from euroleague_insights.euroleague.models import Match
from euroleague_insights.euroleague.models import Play
from euroleague_insights.euroleague.models import Player

logger = logging.getLogger(__name__)

quarter_map = {
    "FirstQuarter": Quarter.FIRST.value,
    "SecondQuarter": Quarter.SECOND.value,
    "ThirdQuarter": Quarter.THIRD.value,
    "ForthQuarter": Quarter.FOURTH.value,
    "ExtraTime": Quarter.EXTRA.value,
}

playtype_map = {pl.value: pl.name for pl in PlayType}

MAX_SECONDS_IN_CLOCK = 59
MAX_TOTAL_SECONDS = 600


def sanitize_value(value: str) -> str | None:
    sanitized_value = value.strip()
    if sanitized_value == "":
        return None
    return sanitized_value


def game_clock_to_seconds(clock):
    if clock is not None:
        minutes, seconds = clock.split(":")
        total_seconds = int(minutes) * 60 + int(seconds)
        if int(minutes) < 0 or int(seconds) < 0:
            msg = "Minutes and seconds cannot be negative"
            raise ValueError(msg)
        if int(seconds) > MAX_SECONDS_IN_CLOCK or total_seconds > MAX_TOTAL_SECONDS:
            msg = "Seconds time limit"
            raise ValueError(msg)
    else:
        total_seconds = ""
    return total_seconds


def create_player(season_code, player_code):
    api = EuroleagueAPI(season=season_code)
    player_data = api.get_individual_player(player_code).get("data", [])
    if len(player_data) == 0:
        logger.info("No data found for player with id %s", player_code)
    if len(player_data) == 1:
        new_player = player_data[0]
        new_player_person = new_player.get("person") or {}
        country = new_player_person.get("country") or {}
        Player.objects.get_or_create(
            code=player_code,
            defaults={
                "fullname": new_player_person.get("name", ""),
                "passport_name": new_player_person.get("passportName", ""),
                "passport_surname": new_player_person.get("passportSurname", ""),
                "jersey_name": new_player_person.get("jerseyName", ""),
                "country_code": country.get("code", ""),
                "country_name": country.get("name", ""),
                "height": new_player_person.get("height", None),
                "weight": new_player_person.get("weight", None),
                "birth_date": new_player_person.get("birthDate", None),
                "type_name": new_player.get("typeName", ""),
            },
        )


@shared_task()
def insert_clubs(season_code):
    api = EuroleagueAPI(season=season_code)
    clubs_data = api.get_clubs().get("data", [])
    logger.info("Fetched %d clubs for season %s", len(clubs_data), season_code)
    for club_datum in clubs_data:
        logger.info("Processing club: %s", club_datum)
        country = club_datum.get("country") or {}
        country_code = country.get("code", "")
        country_name = country.get("name", "")
        Club.objects.update_or_create(
            code=club_datum.get("code", ""),
            defaults={
                "name": club_datum.get("name", ""),
                "alias": club_datum.get("abbreviatedName", ""),
                "country_code": country_code,
                "country_name": country_name,
                "address": club_datum.get("address", ""),
                "city": club_datum.get("city", ""),
            },
        )


@shared_task()
def insert_players(season_code):
    api = EuroleagueAPI(season=season_code)
    players_data = api.get_players().get("data", [])
    logger.info("Fetched %d players for season %s", len(players_data), season_code)
    for new_player in players_data:
        logger.info("Processing player: %s", new_player)
        new_player_person = new_player.get("person") or {}
        country = new_player_person.get("country") or {}
        country_code = country.get("code", "")
        country_name = country.get("name", "")
        Player.objects.update_or_create(
            code=new_player_person.get("code", ""),
            defaults={
                "fullname": new_player_person.get("name", ""),
                "passport_name": new_player_person.get("passportName", ""),
                "passport_surname": new_player_person.get("passportSurname", ""),
                "jersey_name": new_player_person.get("jerseyName", ""),
                "country_code": country_code,
                "country_name": country_name,
                "height": new_player_person.get("height", None),
                "weight": new_player_person.get("weight", None),
                "birth_date": new_player_person.get("birthDate", ""),
                "type_name": new_player.get("typeName", ""),
            },
        )


@shared_task()
def sync_players_current_club(season_code):
    api = EuroleagueAPI(season=season_code)
    players_data = api.get_players().get("data", [])
    logger.info(
        "Synced %d players with current club for season %s",
        len(players_data),
        season_code,
    )
    for player_data in players_data:
        new_player_person = player_data.get("person", {})
        person_code = new_player_person.get("code", "")
        if not person_code:
            continue
        club_data = player_data.get("club", {}) or {}
        club_obj = club_data.get("code", "")
        if club_obj:
            club_obj = Club.objects.get(code=club_obj)
            Player.objects.filter(code=person_code).update(current_club=club_obj)

    logger.info("Synced current clubs for season %s", season_code)


@shared_task()
def insert_matches(season_code):
    api = EuroleagueAPI(season=season_code)
    matches_data = api.get_matches().get("data", [])
    logger.info("Fetched %d matches for season %s", len(matches_data), season_code)
    for new_match in matches_data:
        logger.info("Processing match: %s", new_match)
        new_match_season = new_match.get("season") or {}
        new_match_phase_type = new_match.get("phaseType") or {}
        new_match_local = new_match.get("local") or {}
        new_match_road = new_match.get("road") or {}
        Match.objects.update_or_create(
            match_id=new_match.get("id", ""),
            defaults={
                "game_code": new_match.get("gameCode", ""),
                "name": new_match_season.get("name", ""),
                "phase": new_match_phase_type.get("name", ""),
                "round": new_match.get("round", ""),
                "utc_date": new_match.get("utcDate", ""),
                "local_timezone": new_match.get("localTimeZone", 0),
                "home_team_code": new_match_local.get("club", {}).get("code", ""),
                "away_team_code": new_match_road.get("club", {}).get("code", ""),
                "home_team": new_match_local.get("club", {}).get("name", ""),
                "away_team": new_match_road.get("club", {}).get("name", ""),
                "home_score": new_match_local.get("score", 0),
                "away_score": new_match_road.get("score", 0),
                "venue_name": new_match.get("venue", "").get("name", ""),
                "audience": new_match.get("audience", 0),
            },
        )


@shared_task()
def insert_play(play, season_code, match_id, quarter_name):
    player = None
    player_id = sanitize_value(play.get("PLAYER_ID"))
    if player_id:
        if player_id.startswith("P"):
            player_code = player_id[1:]
            logger.warning(player_code)
            player = Player.objects.filter(code=player_code).first()
            if not player:
                player = create_player(season_code, player_code)
    play_type_code = sanitize_value(play.get("PLAYTYPE", ""))
    play_info = playtype_map.get(play_type_code)
    get_markertime = sanitize_value(play.get("MARKERTIME", None))
    if get_markertime is not None:
        game_seconds = game_clock_to_seconds(get_markertime)
    else:
        game_seconds = None
    match_obj = Match.objects.filter(id=match_id).first()
    Play.objects.update_or_create(
        match=match_obj,
        quarter=quarter_name,
        number_of_play=play.get("NUMBEROFPLAY", 0),
        defaults={
            "play_team": play.get("TEAM", 0),
            "player": player,
            "play_type": play_type_code,
            "game_minute": play.get("MINUTE", 0),
            "game_time": game_seconds,
            "home_team_play_points": play.get("POINTS_A", 0),
            "away_team_play_points": play.get("POINTS_B", 0),
            "play_info": play_info,
        },
    )
    logger.warning(play)


@shared_task(soft_time_limit=1000, time_limit=1200)
def get_match_plays(season_code):
    api = EuroleagueAPI(season=season_code)
    matches = Match.objects.filter().order_by(
        "utc_date",
    )
    for match in matches:
        logger.info("Inserting plays for match %s", match.game_code)
        plays_data_raw = api.get_plays(game_code=match.game_code)
        home_team_code = sanitize_value(plays_data_raw.get("CodeTeamA"))
        away_team_code = sanitize_value(plays_data_raw.get("CodeTeamB"))
        home_team = Club.objects.get(code=home_team_code)
        if not home_team:
            raise ValueError
        away_team = Club.objects.get(code=away_team_code)
        if not away_team:
            raise ValueError
        for quarter_key, quarter_name in quarter_map.items():
            quarter_data = plays_data_raw.get(quarter_key) or []
            logger.info("Processing %s plays in %s", len(quarter_data), quarter_name)
            for play in quarter_data:
                insert_play.delay(play, season_code, match.id, quarter_name)
