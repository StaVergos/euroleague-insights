import httpx

from euroleague_insights.euroleague.euroleague_api.constants import CompetitionCode
from euroleague_insights.euroleague.euroleague_api.constants import EuroleagueApiUrl
from euroleague_insights.euroleague.euroleague_api.constants import EuroleagueLive
from euroleague_insights.euroleague.euroleague_api.constants import SeasonCode


class EuroleagueAPI:
    def __init__(self, season: str):
        self.season = SeasonCode(season)
        self.client = httpx.Client()
        self.live_client = httpx.Client()

    @property
    def api_v2(self) -> str:
        return EuroleagueApiUrl.V2.value

    @property
    def live_api(self) -> str:
        return EuroleagueLive.URL.value

    def euroleague_2024_games_url(self) -> str:
        return (
            f"{self.api_v2}"
            f"/competitions/{CompetitionCode.EUROLEAGUE.value}"
            f"/seasons/{self.season.value}/games"
        )

    def euroleague_clubs_url(self) -> str:
        return (
            f"{self.api_v2}"
            f"/competitions/{CompetitionCode.EUROLEAGUE.value}"
            f"/seasons/{self.season.value}/clubs"
        )

    def euroleague_players_url(self) -> str:
        return (
            f"{self.api_v2}"
            f"/competitions/{CompetitionCode.EUROLEAGUE.value}"
            f"/seasons/{self.season.value}/people"
        )

    def euroleague_matches_url(self) -> str:
        return (
            f"{self.api_v2}"
            f"/competitions/{CompetitionCode.EUROLEAGUE.value}"
            f"/seasons/{self.season.value}/games"
        )

    def euroleague_plays_url(self, game_code) -> str:
        return (
            f"{self.live_api}/PlaybyPlay"
            f"?gamecode={game_code}"
            f"&seasoncode={self.season.value}"
        )

    def euroleague_get_individual_player_url(self, person_code) -> str:
        return (
            f"{self.api_v2}"
            f"/competitions/{CompetitionCode.EUROLEAGUE.value}"
            f"/seasons/{self.season.value}/people/{person_code}"
        )

    def get_clubs(self):
        response = self.client.get(self.euroleague_clubs_url())
        response.raise_for_status()
        return response.json()

    def get_players(self):
        response = self.client.get(self.euroleague_players_url())
        response.raise_for_status()
        return response.json()

    def get_matches(self):
        response = self.client.get(self.euroleague_matches_url())
        response.raise_for_status()
        return response.json()

    def get_plays(self, game_code):
        response = self.client.get(self.euroleague_plays_url(game_code))
        response.raise_for_status()
        return response.json()

    def get_individual_player(self, person_code):
        response = self.client.get(
            self.euroleague_get_individual_player_url(person_code),
        )
        response.raise_for_status()
        return response.json()
