from pydantic import BaseModel

class TeamCreate(BaseModel):
    name: str
    abb: str
    season: int

