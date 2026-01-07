from django.db import models

from euroleague_insights.euroleague.euroleague_api.constants import PhaseType
from euroleague_insights.euroleague.euroleague_api.constants import PlayType
from euroleague_insights.euroleague.euroleague_api.constants import Quarter


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


PLAYTYPE_CHOICES = [(pt.value, pt.value) for pt in PlayType]
QUARTER_CHOICES = [(q.value, q.value) for q in Quarter]


class Play(models.Model):
    id = models.AutoField(primary_key=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="team_play")
    quarter = models.CharField(
        max_length=20,
        choices=QUARTER_CHOICES,
        default=Quarter.FIRST.value,
    )
    number_of_play = models.IntegerField(unique=True)
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    play_team = models.CharField(max_length=50)
    play_type = models.CharField(
        max_length=20,
        choices=PLAYTYPE_CHOICES,
        default=PlayType.BEGIN_PERIOD.value,
    )
    marker_time = models.TimeField(blank=True)
    home_team_play_points = models.IntegerField(null=True, default=None)
    away_team_play_points = models.IntegerField(null=True, default=None)
    play_info = models.CharField(max_length=100, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["match", "number_of_play"],
                name="unique_play_per_match",
            ),
        ]

    def __str__(self):
        return f"Play {self.number_of_play} in Match {self.match.game_code}"

    def set_play_type(self, play_type):
        if isinstance(play_type, PlayType):
            self.play_type = play_type.value

    def set_quarter(self, quarter):
        if isinstance(quarter, Quarter):
            self.quarter = quarter.value
