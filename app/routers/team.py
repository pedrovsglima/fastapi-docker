from fastapi import APIRouter
from ...main import teams

router = APIRouter()

@router.get("/teams/{team_abb}")
def query_team_by_abbreviation(team_abb:str) -> str:
    
    for _,v in enumerate(teams):
        abb = v.get("abbreviation", "")
        if abb == team_abb:
            return v.get("team", "")
        
    return f"No team has the following abbreviation: {team_abb}"


@router.get("/teams/")
def query_team_by_parameters(abb:str, season:str) -> dict:

    for _,v in enumerate(teams):
        current_abb = v.get("abbreviation", "")
        current_season = v.get("season", "")
        if current_abb == abb and current_season == season:
            return {
                "abbreviation": v.get("abbreviation", ""),
                "team": v.get("team", ""),
                "season": v.get("season", ""),
                "age": v.get("age", ""),
            }

    return {"message": f"No team from season {season} has the abbreviation {abb}"}


@router.post("/teams/")
def add_team(name:str, abb:str, season:str) -> dict:
    
    for _,v in enumerate(teams):
        current_name = v.get("team", "")
        current_abb = v.get("abbreviation", "")
        current_season = v.get("season", "")
        if current_name == name and current_abb == abb and current_season == season:
            return {
                "message": "Team already exists"
            }

    teams_old = teams.copy()

    new_team = {
        "season": season,	
        "lg": "NBA",	
        "team": name,	
        "abbreviation": abb,	
        "playoff": "FALSE",
    }
    teams.append(new_team)

    return {
        "len_before": len(teams_old),
        "len_after": len(teams),
        "new_team": new_team,
    }


@router.delete("/teams/{team_abb}")
def delete_team(team_abb:str) -> dict:

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