from enum import StrEnum


class EuroleagueAPIURL(StrEnum):
    V2 = "https://api-live.euroleague.net/v2"
    V3 = "https://api-live.euroleague.net/v3"


class EuroleagueLive(StrEnum):
    URL = "https://live.euroleague.net/api"


class PhaseType(StrEnum):
    REGULAR_SEASON = "Regular Season"
    PLAYOFFS = "Playoffs"
    FINAL_FOUR = "Final Four"


class CompetitionCode(StrEnum):
    EUROLEAGUE = "E"


class SeasonCode(StrEnum):
    E2024 = "E2024"
    E2023 = "E2023"


class PlayType(StrEnum):
    BEGIN_PERIOD = "BP"
    JUMP_BALL = "JB"
    THREE_POINT_FIELD_GOAL = "3FG"
    DEFENSIVE_REBOUND = "D"
    TWO_POINT_FIELD_GOAL = "2FG"
    OFFENSIVE_REBOUND = "O"
    TWO_POINT_FIELD_GOAL_MADE = "2FGM"
    END_GAME = "EG"


class PositionName(StrEnum):
    GUARD = "Guard"
    FORWARD = "Forward"
    CENTER = "Center"
