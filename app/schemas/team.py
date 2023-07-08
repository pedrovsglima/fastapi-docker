from typing import Optional
from pydantic import BaseModel

class TeamCreate(BaseModel):
    team: str
    abb: str
    season: int

class TeamBasicInfo(BaseModel):
    season: int
    team: str
    abbreviation: str
    playoffs: Optional[bool]
    age: Optional[float]

    class Config:
        orm_mode = True

class TeamAndSeason(BaseModel):
    abb: str
    season: Optional[int]