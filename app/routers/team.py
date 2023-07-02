from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
from database import get_db

router = APIRouter(prefix="/teams", tags=["teams"])

@router.get("/{team_abb}")
def query_team_by_abbreviation(team_abb:str, db:Session=Depends(get_db)) -> dict:

    result = (
        db.query(models.TeamSummary.season, models.TeamSummary.team, models.TeamSummary.age)
        .filter(models.TeamSummary.abbreviation==team_abb)
        .first()
    )

    if result:
        return {"data": result}
    else:
        return {"message": f"No team has the following abbreviation: {team_abb}"}


# @router.get("/")
# def query_team_by_parameters(abb:str, season:str) -> dict:

#     for _,v in enumerate(teams):
#         current_abb = v.get("abbreviation", "")
#         current_season = v.get("season", "")
#         if current_abb == abb and current_season == season:
#             return {
#                 "abbreviation": v.get("abbreviation", ""),
#                 "team": v.get("team", ""),
#                 "season": v.get("season", ""),
#                 "age": v.get("age", ""),
#             }

#     return {"message": f"No team from season {season} has the abbreviation {abb}"}


# @router.post("/")
# def add_team(name:str, abb:str, season:str) -> dict:
    
#     for _,v in enumerate(teams):
#         current_season = v.get("season", "")
#         current_name = v.get("team", "")
#         current_abb = v.get("abbreviation", "")
#         if current_name == name and current_abb == abb and current_season == season:
#             return {
#                 "message": "Team already exists"
#             }

#     teams_old = teams.copy()

#     new_team = {
#         "season": season,	
#         "lg": "NBA",	
#         "team": name,	
#         "abbreviation": abb,	
#         "playoff": "FALSE",
#     }
#     teams.append(new_team)

#     return {
#         "len_before": len(teams_old),
#         "len_after": len(teams),
#         "new_team": new_team,
#     }


# @router.delete("/{team_abb}")
# def delete_team(team_abb:str) -> dict:

    teams_old = teams.copy()

    for i,v in enumerate(teams):
        current_abb = v.get("abbreviation", "")
        if current_abb == team_abb:
            deleted_team = teams.pop(i)
            return {
                "len_before": len(teams_old),
                "len_after": len(teams),
                "deleted_team": deleted_team,
            }
    
    return {
        "message": "Team does not exist"
    }