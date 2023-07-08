from typing import Optional
from pydantic import BaseModel

class PlayerInfoResponse(BaseModel):

    player_id: int
    player: str
    birth_year: Optional[int]
    hof: Optional[bool]
    num_seasons: int
    first_seas: int
    last_seas: int

    class Config:
        orm_mode = True


class PlayerAndSeason(BaseModel):
    id: int
    season: Optional[int]