from rest_framework import serializers
from euroleague_insights.euroleague.models import Player, Club


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = (
            "id",
            "code",
            "name",
            "alias",
            "country_code",
            "country_name",
            "address",
            "city",
        )


class PlayerSerializer(serializers.ModelSerializer):
    current_club = serializers.CharField(
        source="current_club.name", read_only=True, allow_blank=True, allow_null=True
    )

    class Meta:
        model = Player
        fields = (
            "id",
            "code",
            "fullname",
            "passport_name",
            "passport_surname",
            "jersey_name",
            "country_code",
            "country_name",
            "height",
            "weight",
            "birth_date",
            "current_club",
        )
        read_only_fields = ("id", "current_club")
