import logging

from euroleague_insights.euroleague.models import Club
from euroleague_insights.euroleague.tasks import insert_clubs

logger = logging.getLogger(__name__)


def list_clubs():
    return Club.objects.all()
