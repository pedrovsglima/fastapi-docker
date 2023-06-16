import json
import pandas as pd
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from http.client import HTTPException

app = FastAPI()

# def csv_to_dict(file:str, cols:List[str]=None) -> dict:
#     df = pd.read_csv(
#             file,
#             delimiter=",",
#             usecols=cols,
#         ).drop_duplicates(inplace=True)
    
#     return df.to_dict("records")

@app.get("/")
def index() -> dict:
    return {"status": "OK"}

@app.get("/teams/{team_abb}")
def query_team_by_abbreviation(team_abb:str) -> str:
    
    teams = json.load(open("teams.json"))
    
    for _,v in enumerate(teams):
        abb = v.get("abbreviation", "")
        if abb == team_abb:
            return v.get("team", "")
        
    return f"No team has the abbreviation: {team_abb}"    

    # teams = csv_to_dict(
    #     file="./nba-stats/team-summaries.csv", 
    #     cols=["team", "abbreviation"]
    # )

    # team = teams[teams["abbreviation"]==team_abb]
    
    # if team.empty:
    #     raise HTTPException(
    #         status_code=404,
    #         detail=f"No team has the abbreviation: {team_abb}"
    #     )
    
    # return team["team"]