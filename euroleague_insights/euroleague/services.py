import logging

from euroleague_insights.euroleague.models import Club
from euroleague_insights.euroleague.models import Player

logger = logging.getLogger(__name__)


def list_clubs():
    return Club.objects.order_by("id")


def list_players():
    return Player.objects.order_by("id")


def list_club_players(code):
    try:
        club = Club.objects.get(code=code)
    except Club.DoesNotExist:
        logger.exception("Club with code %s does not exist", code)
        return Player.objects.none()

    return Player.objects.filter(current_club=club).order_by("id")
