import logging

from euroleague_insights.euroleague.models import Club
from euroleague_insights.euroleague.tasks import insert_clubs

logger = logging.getLogger(__name__)


def list_clubs(season_code="E2024"):
    insert_clubs.delay(season_code=season_code)
    return Club.objects.all()
