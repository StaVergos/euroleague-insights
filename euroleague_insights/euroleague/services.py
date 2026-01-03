import logging

from django.db.models import Q

from euroleague_insights.euroleague.models import Club
from euroleague_insights.euroleague.models import Match
from euroleague_insights.euroleague.models import Player

logger = logging.getLogger(__name__)


def list_clubs():
    return Club.objects.order_by("id")


def list_players():
    return Player.objects.order_by("id")


def list_club_players(club_code):
    try:
        club = Club.objects.get(code=club_code)
    except Club.DoesNotExist:
        logger.exception("Club with code %s does not exist", club_code)
        return Player.objects.none()

    return Player.objects.filter(current_club=club).order_by("id")


def list_matches():
    return Match.objects.order_by("round")


def list_club_matches(club_match_code):
    try:
        Club.objects.get(code=club_match_code)
    except Club.DoesNotExist:
        logger.exception("Club with code %s does not exist", club_match_code)
        return Match.objects.none()

    return Match.objects.filter(
        Q(home_team_code=club_match_code) | Q(away_team_code=club_match_code),
    ).order_by("round")
