from src.euroleague.api import EuroleagueAPI
from src.euroleague.schemas.clubs import Club, DTOClub


class EuroleagueService:
    def __init__(self, api: EuroleagueAPI) -> None:
        self.api = api

    def normalize_club_data(self, clubs: list[Club]) -> list[DTOClub]:
        dto_clubs = []
        for club in clubs:
            dto_club = DTOClub(
                code=club.tv_code,
                name=club.name,
                crest_image=club.images.crest,
                original_name=club.original_name,
                original_alias=club.original_alias,
                country_code=club.country.code,
                city=club.city.title(),
                venue_code=club.venue_code,
            )
            dto_clubs.append(dto_club)
        return dto_clubs

    async def get_clubs(self) -> list[DTOClub]:
        club_response = await self.api.get_clubs()
        return self.normalize_club_data(club_response.data)
