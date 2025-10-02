from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column
from src.db.base import Base, TimestampMixin


class Club(TimestampMixin, Base):
    __tablename__ = "clubs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text)
    code: Mapped[str] = mapped_column(Text, unique=True, index=True)
    crest_image: Mapped[str] = mapped_column(Text)
    original_name: Mapped[str] = mapped_column(Text)
    original_alias: Mapped[str] = mapped_column(Text)
    country_code: Mapped[str] = mapped_column(Text)
    city: Mapped[str] = mapped_column(Text)
    venue_code: Mapped[str] = mapped_column(Text)
