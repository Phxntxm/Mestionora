from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

from src.models.clubs import Club, ClubMember