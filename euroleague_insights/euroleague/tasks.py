import logging

from celery import shared_task

from euroleague_insights.euroleague.euroleague_api.api import EuroleagueAPI
from euroleague_insights.euroleague.euroleague_api.constants import SeasonCode
from euroleague_insights.euroleague.models import Club

logger = logging.getLogger(__name__)


@shared_task()
def insert_clubs(season_code):
    api = EuroleagueAPI()
    season = SeasonCode(season_code)
    clubs_data = api.get_clubs(season).get("data", [])
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
