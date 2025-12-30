import logging

from euroleague_insights.euroleague.models import Club
from euroleague_insights.euroleague.models import Player

logger = logging.getLogger(__name__)


def list_clubs():
    return Club.objects.order_by("id")


def list_players():
    return Player.objects.order_by("id")
