from pydantic import BaseModel, Field, HttpUrl


class ClubImage(BaseModel):
    crest: HttpUrl = Field(
        examples=[
            "https://media-cdn.cortextech.io/9a463aa2-ceb2-481c-9a95-1cddee0a248e.png"
        ]
    )


class Country(BaseModel):
    code: str = Field(min_length=3, max_length=3, examples=["TUR"])
    name: str = Field(examples=["Turkiye"])


class Club(BaseModel):
    code: str = Field(min_length=3, max_length=3, examples=["IST"])
    name: str = Field(examples=["Anadolu Efes Istanbul"])
    abbreviated_name: str = Field(
        validation_alias="abbreviatedName", examples=["Anadolu Efes"]
    )
    editoral_name: str = Field(
        validation_alias="editorialName", examples=["Anadolu Efes"]
    )
    tv_code: str = Field(
        min_length=3, max_length=3, validation_alias="tvCode", examples=["EFS"]
    )
    is_virtual: bool = Field(validation_alias="isVirtual", examples=["false"])
    images: ClubImage
    sponsor: str = Field(examples=["Anadolu Efes Istanbul"])
    original_name: str = Field(
        validation_alias="clubPermanentName", examples=["Anadolu Efes Istanbul"]
    )
    original_alias: str = Field(
        validation_alias="clubPermanentAlias", examples=["Anadolu Efes"]
    )
    country: Country
    address: str = Field(
        examples=[
            "Mahmutbey Mahallesi Ordu Caddesi 2581. Sokak No:3 - Bagcılar 34218 Istanbul "
        ]
    )
    website: HttpUrl = Field(examples=["https://www.anadoluefessk.org/"])
    tickets_url: HttpUrl = Field(
        validation_alias="ticketsUrl",
        examples=["https://www.anadoluefessk.org/en/tickets"],
    )
    twitter_account: str = Field(
        validation_alias="twitterAccount", examples=["AnadoluEfesSK"]
    )
    venue_code: str = Field(validation_alias="venueCode", examples=["AVG"])
    city: str = Field(examples=["ISTANBUL"])
    president: str = Field(examples=["Tuncay Ozilhan"])
    phone: str = Field(examples=["+90 212 449 38 84"])


class DTOClub(BaseModel):
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


class ClubResponse(BaseModel):
    data: list[Club]
    total: int = Field(examples=["18"])
