from django.core.management.base import BaseCommand

from euroleague_insights.euroleague.tasks import insert_matches


class Command(BaseCommand):
    help = "Seed players into the database."

    def handle(self, *args, **options):
        self.stdout.write("Seeding matches...")
        insert_matches.delay(season_code="E2025")
        self.stdout.write(self.style.SUCCESS("Successfuly seeded matches."))
