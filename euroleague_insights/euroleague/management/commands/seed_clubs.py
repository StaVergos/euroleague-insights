from django.core.management.base import BaseCommand

from euroleague_insights.euroleague.tasks import insert_clubs


class Command(BaseCommand):
    help = "Seed clubs into the database."

    def handle(self, *args, **options):
        self.stdout.write("Seeding clubs...")
        insert_clubs.delay(season_code="E2025")
        self.stdout.write(self.style.SUCCESS("Successfully seeded clubs."))
