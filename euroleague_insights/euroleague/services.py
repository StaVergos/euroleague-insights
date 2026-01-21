import logging

from django.db.models import Case
from django.db.models import ExpressionWrapper
from django.db.models import F
from django.db.models import IntegerField
from django.db.models import Q
from django.db.models import Sum
from django.db.models import Value
from django.db.models import When

from euroleague_insights.euroleague.euroleague_api.constants import PlayType
from euroleague_insights.euroleague.models import Club
from euroleague_insights.euroleague.models import Match
from euroleague_insights.euroleague.models import Play
from euroleague_insights.euroleague.models import Player

logger = logging.getLogger(__name__)


def list_clubs():
    return Club.objects.order_by("id")


def list_players():
    return Player.objects.filter(type_name="Player").order_by("id")


def list_club_players(club_code):
    try:
        club = Club.objects.get(code=club_code)
    except Club.DoesNotExist:
        logger.exception("Club with code %s does not exist", club_code)
        return Player.objects.none()

    return Player.objects.filter(current_club=club).order_by("id")


def list_matches():
    return Match.objects.order_by("round", "game_code")


def list_club_matches(club_code):
    try:
        Club.objects.get(code=club_code)
    except Club.DoesNotExist:
        logger.exception("Club with code %s does not exist", club_code)
        return Match.objects.none()

    return Match.objects.filter(
        Q(home_team_code=club_code) | Q(away_team_code=club_code),
    ).order_by("round")


def list_plays(game_code):
    return Play.objects.filter(match__game_code=game_code).order_by("number_of_play")


def list_match_top_scorers(game_code, limit=10):
    scoring_play_types = [
        PlayType.FREE_THROW_MADE.value,
        PlayType.TWO_POINT_FIELD_GOAL_MADE.value,
        PlayType.THREE_POINT_FIELD_GOAL_MADE.value,
    ]
    return (
        Play.objects.filter(
            match__game_code=game_code,
            play_type__in=scoring_play_types,
            player__isnull=False,
        )
        .values(
            code=F("player__code"),
            name=F("player__fullname"),
            club_name=F("player__current_club__name"),
        )
        .annotate(
            free_throws=Sum(
                Case(
                    When(
                        play_type=PlayType.FREE_THROW_MADE.value,
                        then=Value(1),
                    ),
                    default=Value(0),
                    output_field=IntegerField(),
                ),
            ),
            two_pointers=Sum(
                Case(
                    When(
                        play_type=PlayType.TWO_POINT_FIELD_GOAL_MADE.value,
                        then=Value(1),
                    ),
                    default=Value(0),
                    output_field=IntegerField(),
                ),
            ),
            three_pointers=Sum(
                Case(
                    When(
                        play_type=PlayType.THREE_POINT_FIELD_GOAL_MADE.value,
                        then=Value(1),
                    ),
                    default=Value(0),
                    output_field=IntegerField(),
                ),
            ),
        )
        .annotate(
            score=ExpressionWrapper(
                F("free_throws") + F("two_pointers") * 2 + F("three_pointers") * 3,
                output_field=IntegerField(),
            ),
        )
        .order_by("-score", "name")[:limit]
    )
