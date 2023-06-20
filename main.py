from csv import DictReader
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index() -> dict:
    return {"status": "OK"}

@app.get("/teams/{team_abb}")
def query_team_by_abbreviation(team_abb:str) -> str:
    
    with open("./nba-stats/team-summaries.csv","r") as f:
        teams = list(DictReader(f))
    
    for _,v in enumerate(teams):
        abb = v.get("abbreviation", "")
        if abb == team_abb:
            return v.get("team", "")
        
    return f"No team has the following abbreviation: {team_abb}"