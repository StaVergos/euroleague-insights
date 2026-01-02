import logging

from euroleague_insights.euroleague.models import Club, Player

logger = logging.getLogger(__name__)


def list_clubs():
    return Club.objects.order_by("id")


def list_players():
    return Player.objects.order_by("id")


def list_club_players(club_code):
    try:
        club = Club.objects.get(club_code=club_code)
    except Club.DoesNotExist:
        logger.exception("Club with code %s does not exist", club_code)
        return Player.objects.none()

    return Player.objects.filter(current_club=club).order_by("id")
