from rest_framework import serializers

from euroleague_insights.euroleague.euroleague_api.constants import PhaseType


class ClubSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    code = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=255)
    alias = serializers.CharField(max_length=100)
    country_code = serializers.CharField(max_length=3)
    country_name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=255, allow_null=True, default=None)
    city = serializers.CharField(max_length=100, allow_null=True, default=None)


class PlayerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    code = serializers.CharField(max_length=10)
    fullname = serializers.CharField(max_length=50)
    passport_name = serializers.CharField(max_length=50)
    passport_surname = serializers.CharField(max_length=50)
    jersey_name = serializers.CharField(max_length=50, allow_null=True, default=None)
    country_code = serializers.CharField(max_length=3)
    country_name = serializers.CharField(max_length=100)
    height = serializers.IntegerField()
    weight = serializers.IntegerField()
    birth_date = serializers.DateTimeField()
    current_club = serializers.CharField(allow_null=True, default=None)


class MatchSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    match_id = serializers.CharField(max_length=100)
    game_code = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    phase = serializers.ChoiceField(choices=[(p.value, p.value) for p in PhaseType])
    round = serializers.IntegerField()
    utc_date = serializers.DateTimeField()
    local_timezone = serializers.IntegerField()
    home_team_code = serializers.CharField(max_length=3)
    away_team_code = serializers.CharField(max_length=3)
    home_team = serializers.CharField(max_length=50)
    away_team = serializers.CharField(max_length=50)
    home_score = serializers.IntegerField(allow_null=True, default=None)
    away_score = serializers.IntegerField(allow_null=True, default=None)
    venue_name = serializers.CharField(max_length=100)
    audience = serializers.IntegerField(allow_null=True, default=None)
