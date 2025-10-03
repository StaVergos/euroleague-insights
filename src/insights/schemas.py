from pydantic import BaseModel, Field, HttpUrl, ConfigDict


class DTOClub(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None
    code: str = Field(min_length=3, max_length=3, examples=["EFS"])
    name: str = Field(examples=["Anadolu Efes Istanbul"])
    crest_image: HttpUrl = Field(
        examples=[
            "https://media-cdn.cortextech.io/9a463aa2-ceb2-481c-9a95-1cddee0a248e.png"
        ]
    )
    original_name: str = Field(examples=["Anadolu Efes Istanbul"])
    original_alias: str = Field(examples=["Anadolu Efes"])
    country_code: str = Field(min_length=3, max_length=3, examples=["TUR"])
    city: str = Field(examples=["Istanbul"])
    venue_code: str = Field(examples=["AVG"])
