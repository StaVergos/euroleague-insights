from django.contrib import admin

from euroleague_insights.euroleague.models import Club


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "country_name", "city")
    search_fields = ("name", "code", "country_name", "city")
