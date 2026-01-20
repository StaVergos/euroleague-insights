from celery import chain
from django.core.management.base import BaseCommand

from euroleague_insights.euroleague.tasks import get_match_plays
from euroleague_insights.euroleague.tasks import insert_clubs
from euroleague_insights.euroleague.tasks import insert_matches
from euroleague_insights.euroleague.tasks import insert_players
from euroleague_insights.euroleague.tasks import sync_players_current_club


class Command(BaseCommand):
    help = "Seed euroleague data into the database."

    def handle(self, *args, **options):
        season_code = "E2025"
        self.stdout.write("Seeding euroleague data...")
        res = chain(
            insert_clubs(season_code),
            insert_players(season_code),
            sync_players_current_club(season_code),
            insert_matches(season_code),
            get_match_plays(season_code),
        )()
        res.get()
        self.stdout.write(self.style.SUCCESS("Successfully seeded euroleague data."))
