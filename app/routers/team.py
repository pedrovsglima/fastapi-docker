from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
from database import get_db

router = APIRouter(prefix="/teams", tags=["teams"])

@router.get("/{team_abb}")
def query_team_by_abbreviation(team_abb:str, db:Session=Depends(get_db)) -> dict:

    result = (
        db.query(models.TeamSummary)
        .filter(models.TeamSummary.abbreviation==team_abb)
        .first()
    )

    if result:
        return {"data": result}
    else:
        return {"message": f"No team has the following abbreviation: {team_abb}"}


@router.get("/")
def query_team_by_parameters(abb:str, season:str, db:Session=Depends(get_db)) -> dict:

    result = (
        db.query(models.TeamSummary)
        .filter(
            models.TeamSummary.abbreviation==abb, 
            models.TeamSummary.season==season,
        )
        .first()
    )

    if result:
        return {"data": result}
    else:
        return {"message": f"No team from season {season} has the abbreviation {abb}"}


@router.post("/")
def add_team(name:str, abb:str, season:str, db:Session=Depends(get_db)) -> dict:

    result = (
        db.query(models.TeamSummary)
        .filter(
            models.TeamSummary.abbreviation==abb,
            models.TeamSummary.season==season,
            models.TeamSummary.team==name,
        )
        .first()
    )

    if result:
        return {"message": "Team already exists"}
    
    else:
        new_team = models.TeamSummary(season=season, team=name, abbreviation=abb)
        db.add(new_team)
        db.commit()
        db.refresh(new_team)

        return {"data": new_team}


@router.delete("/{team_abb}")
def delete_team(team_abb:str, db:Session=Depends(get_db)) -> dict:

    team_query = (
        db.query(models.TeamSummary)
        .filter(models.TeamSummary.abbreviation==team_abb)
    )

    if not team_query.first():
        return {"message": "Team does not exist"}
    
    else:
        team_query.delete(synchronize_session=False)
        db.commit()
        return {"data": "Team deleted"}