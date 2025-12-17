import logging

from celery import shared_task

from euroleague_insights.euroleague.euroleague_api.api import EuroleagueAPI
from euroleague_insights.euroleague.models import Club
from euroleague_insights.euroleague.models import Player

logger = logging.getLogger(__name__)


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
            },
        )
