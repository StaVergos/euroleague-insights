from enum import StrEnum


class EuroleagueApiUrl(StrEnum):
    V1 = "https://api-live.euroleague.net/v1"
    V2 = "https://api-live.euroleague.net/v2"
    V3 = "https://api-live.euroleague.net/v3"


class EuroleagueLive(StrEnum):
    URL = "https://live.euroleague.net/api"


class PhaseType(StrEnum):
    REGULAR_SEASON = "Regular Season"
    PLAY_IN = "Play-In"
    PLAYOFFS = "Playoffs"
    FINAL_FOUR = "Final Four"


class CompetitionCode(StrEnum):
    EUROLEAGUE = "E"


class SeasonCode(StrEnum):
    E2023 = "E2023"
    E2024 = "E2024"
    E2025 = "E2025"


class PlayType(StrEnum):
    BEGIN_PERIOD = "BP"
    END_PERIOD = "EP"
    JUMP_BALL = "JB"
    FREE_THROW_ATTEMPT = "FTA"
    FREE_THROW_MADE = "FTM"
    TWO_POINT_FIELD_GOAL = "2FGA"
    TWO_POINT_FIELD_GOAL_MADE = "2FGM"
    THREE_POINT_FIELD_GOAL_ATTEMPT = "3FGA"
    THREE_POINT_FIELD_GOAL_MADE = "3FGM"
    DEFENSIVE_REBOUND = "D"
    OFFENSIVE_REBOUND = "O"
    TURNOVER = "TO"
    ASSIST = "AS"
    BLOCK = "FV"
    STEAL = "ST"
    FOUL = "CM"
    FOUL_DRAWN = "FV"
    OFFENSIVE_FOUL = "OF"
    TIMEOUT = "TOUT"
    TV_TIMEOUT = "TOUT-TV"
    TECHNICAL_FOUL = "CMT"
    UNSPORTSMANLIKE_FOUL = "CMU"
    IN = "IN"
    OUT = "OUT"
    END_GAME = "EG"


class PositionName(StrEnum):
    GUARD = "Guard"
    FORWARD = "Forward"
    CENTER = "Center"


class Quarter(StrEnum):
    FIRST = "First Quarter"
    SECOND = "Second Quarter"
    THIRD = "Third Quarter"
    FOURTH = "Fourth Quarter"
    EXTRA = "Extra Time"
