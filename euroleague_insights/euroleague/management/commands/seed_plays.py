from django.core.management.base import BaseCommand

from euroleague_insights.euroleague.tasks import get_match_plays


class Command(BaseCommand):
    help = "Sync plays from euroleague matches."

    def handle(self, *args, **options):
        self.stdout.write("Syncing plays ...")
        get_match_plays.delay(season_code="E2025")
        self.stdout.write(
            self.style.SUCCESS("Successfully synced plays."),
        )
