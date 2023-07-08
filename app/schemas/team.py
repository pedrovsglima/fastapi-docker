from typing import Optional
from pydantic import BaseModel

class TeamCreate(BaseModel):
    team: str
    abb: str
    season: int

class TeamResponse(BaseModel):
    season: int
    lg: Optional[str]
    team: str
    abbreviation: str
    playoffs: Optional[bool]
    age: Optional[float]

    class Config:
        orm_mode = True