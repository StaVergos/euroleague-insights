import httpx
from src.euroleague.constants import (
    EuroleagueAPIURL,
    CompetitionCode,
    SeasonCode,
    EuroleagueLive,
)
from src.euroleague.schemas.clubs import ClubResponse


class EuroleagueAPI:
    def __init__(self):
        self.client = httpx.Client()

    @property
    def api_v2(self) -> str:
        return EuroleagueAPIURL.V2.value

    @property
    def euroleague_2024_games_url(self) -> str:
        return (
            f"{self.api_v2}"
            f"/competitions/{CompetitionCode.EUROLEAGUE.value}"
            f"/seasons/{SeasonCode.E2024.value}/games"
        )

    @property
    def euroleague_2024_clubs_url(self) -> str:
        return (
            f"{self.api_v2}"
            f"/competitions/{CompetitionCode.EUROLEAGUE.value}"
            f"/seasons/{SeasonCode.E2024.value}/clubs"
        )

    def euroleague_players_url(
        self,
        competition_code: str = CompetitionCode.EUROLEAGUE.value,
        season_code: str = SeasonCode.E2024.value,
    ) -> str:
        return (
            f"{self.api_v2}"
            f"/competitions/{competition_code}"
            f"/players?seasonCode={season_code}"
        )

    def euroleague_play_by_play_url(self, game_code: int, season_code: str) -> str:
        return (
            f"{EuroleagueLive.URL}"
            f"/PlaybyPlay?gamecode={game_code}&seasoncode={season_code}"
        )

    def euroleague_box_score_url(self, game_code: int, season_code: str) -> str:
        return (
            f"{EuroleagueLive.URL}"
            f"/Boxscore?gamecode={game_code}&seasoncode={season_code}"
        )

    def get_clubs(self) -> ClubResponse:
        resp = self.client.get(self.euroleague_2024_clubs_url)
        resp.raise_for_status()

        result = resp.json()
        club_response = ClubResponse.model_validate(result)

        return club_response
