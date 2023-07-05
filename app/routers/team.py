from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

import models
import schemas
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No team has the abbreviation {team_abb}")


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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No team from season {season} has the abbreviation {abb}"
        )


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_team(team:schemas.TeamCreate, db:Session=Depends(get_db)) -> dict:

    result = (
        db.query(models.TeamSummary)
        .filter(
            models.TeamSummary.abbreviation==team.abb,
            models.TeamSummary.season==team.season,
            models.TeamSummary.team==team.name,
        )
        .first()
    )

    if result:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Team already exists")
    
    else:
        new_team = models.TeamSummary(
            season=team.season, team=team.name, abbreviation=team.abb)
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Team does not exist")
    
    else:
        team_query.delete(synchronize_session=False)
        db.commit()
        return {"data": "Team deleted"}