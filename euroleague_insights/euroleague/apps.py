from django.apps import AppConfig


class EuroleagueConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    # App path must match the package location so Django can register models
    name = "euroleague_insights.euroleague"
