from http.client import HTTPException
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/teams/{team_abb}")
def query_team_by_abbreviation(team_abb:str) -> str:
    teams = pd.read_csv(
        "./nba-stats/team-summaries.csv",
        delimiter=",",
        usecols=["team", "abbreviation"]
    ).drop_duplicates(inplace=True)

    team = teams[teams["abbreviation"]==team_abb]
    
    if team.empty:
        raise HTTPException(
            status_code=404,
            detail=f"No team has the abbreviation: {team_abb}"
        )
    
    return team["team"]