from django.core.management.base import BaseCommand

from euroleague_insights.euroleague.tasks import sync_players_current_club


class Command(BaseCommand):
    help = "Sync players current clubs."

    def handle(self, *args, **options):
        self.stdout.write("Syncing players current clubs...")
        sync_players_current_club.delay(season_code="E2025")
        self.stdout.write(
            self.style.SUCCESS("Successfully synced players current clubs."),
        )
