from django.db import models

from euroleague_insights.euroleague.euroleague_api.constants import PhaseType


class Club(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True)
    country_code = models.CharField(max_length=3, blank=True)
    country_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, unique=True)
    fullname = models.CharField(max_length=50)
    passport_name = models.CharField(max_length=50, blank=True)
    passport_surname = models.CharField(max_length=50, blank=True)
    jersey_name = models.CharField(max_length=50, null=True, blank=True)
    country_code = models.CharField(max_length=3)
    country_name = models.CharField(max_length=100)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    birth_date = models.DateTimeField(blank=True)
    current_club = models.ForeignKey(
        Club,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.fullname


PHASE_CHOICES = [(p.value, p.value) for p in PhaseType]


class Match(models.Model):
    id = models.AutoField(primary_key=True)
    match_id = models.CharField(max_length=100, unique=True)
    game_code = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    phase = models.CharField(
        max_length=20,
        choices=PHASE_CHOICES,
        default=PhaseType.REGULAR_SEASON.value,
    )
    round = models.IntegerField()
    utc_date = models.DateTimeField()
    local_timezone = models.IntegerField()
    home_team_code = models.CharField(max_length=3)
    away_team_code = models.CharField(max_length=3)
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    home_score = models.IntegerField(null=True, default=None)
    away_score = models.IntegerField(null=True, default=None)
    venue_name = models.CharField(max_length=100)
    audience = models.IntegerField(null=True, default=None)

    def __str__(self):
        return self.match_id

    def set_phase_type(self, phase_type):
        if isinstance(phase_type, PhaseType):
            self.phase = phase_type.value
