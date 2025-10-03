from src.db.models import Club
from src.euroleague.schemas.clubs import ClubResponse, Club as ClubSchema
from src.euroleague.service import EuroleagueService
from src.insights.schemas import DTOClub


class InsightsService:
    def __init__(self, euroleague_service: EuroleagueService, db) -> None:
        self.euroleague_service = euroleague_service
        self.db = db

    async def get_clubs_from_euroleague(self) -> list[DTOClub]:
        if self.db.query(Club).count() > 0:
            clubs = self.db.query(Club).all()
            return [DTOClub.from_orm(club) for club in clubs]
        club_response = await self.euroleague_service.get_clubs()
        clubs = []
        for club_data in club_response.data:
            club = Club(
                name=club_data.name,
                code=club_data.code,
                crest_image=str(club_data.images.crest),
                original_name=club_data.original_name,
                original_alias=club_data.original_alias,
                country_code=club_data.country.code,
                city=club_data.city,
                venue_code=club_data.venue_code,
            )
            clubs.append(club)
        self.db.add_all(clubs)
        self.db.commit()
        return [DTOClub.model_validate(club) for club in clubs]

    async def get_clubs(self) -> list[DTOClub]:
        clubs = self.db.query(Club).all()
        return [DTOClub.model_validate(club) for club in clubs]
