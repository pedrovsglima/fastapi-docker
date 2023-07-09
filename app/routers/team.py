from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter(prefix="/teams", tags=["teams"])


@router.get("/", response_model=schemas.TeamBasicInfo)
def query_team_by_parameters(abb:str, season:str, db:Session=Depends(get_db)):

    result = (
        db.query(models.TeamSummary)
        .filter(
            models.TeamSummary.abbreviation==abb, 
            models.TeamSummary.season==season,
        )
        .first()
    )

    if result:
        return result
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No team from season {season} has the abbreviation {abb}"
        )


@router.get("/stats-per-game")
def stats_per_game(team:schemas.TeamAndSeason, db:Session=Depends(get_db)):

    query_filter = [models.TeamStatsPerGame.abbreviation==team.abb]
    if team.season:
        query_filter.append(models.TeamStatsPerGame.season==team.season)

    result = db.query(models.TeamStatsPerGame).filter(*query_filter).all()

    if result:
        return result
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No team found. Abbreviation: {team.abb}, Season: {team.season}"
        )


@router.get("/totals")
def stats_totals(team:schemas.TeamAndSeason, db:Session=Depends(get_db)):

    query_filter = [models.TeamTotal.abbreviation==team.abb]
    if team.season:
        query_filter.append(models.TeamTotal.season==team.season)

    result = db.query(models.TeamTotal).filter(*query_filter).all()

    if result:
        return result
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No team found. Abbreviation: {team.abb}, Season: {team.season}"
        )


@router.get("/{team_abb}", response_model=List[schemas.TeamBasicInfo])
def query_team_by_abbreviation(team_abb:str, db:Session=Depends(get_db)):

    result = (
        db.query(models.TeamSummary)
        .filter(models.TeamSummary.abbreviation==team_abb)
        .all()
    )

    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No team has the abbreviation {team_abb}")


@router.get("/season/{season}")
def list_teams_by_season(season:int, db:Session=Depends(get_db)):

    result = (
        db.query(models.TeamSummary)
        .filter(models.TeamSummary.season==season)
        .all()
    )

    if result:
        return result
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No team on season {season}"
        )


@router.get("/end-of-season/{season}")
def list_end_of_season_teams(season:int, db:Session=Depends(get_db)):

    result = (
        db.query(models.TeamEndOfSeason)
        .filter(models.TeamEndOfSeason.season==season)
        .all()
    )

    if result:
        return result
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No team on season {season}"
        )


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.TeamBasicInfo)
def add_team(team:schemas.TeamCreate, db:Session=Depends(get_db)):

    result = (
        db.query(models.TeamSummary)
        .filter(
            models.TeamSummary.abbreviation==team.abb,
            models.TeamSummary.season==team.season,
            models.TeamSummary.team==team.team,
        )
        .first()
    )

    if result:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Team already exists")
    
    else:
        new_team = models.TeamSummary(
            season=team.season, team=team.team, abbreviation=team.abb)
        db.add(new_team)
        db.commit()
        db.refresh(new_team)

        return new_team


@router.delete("/{team_abb}")
def delete_team(team_abb:str, db:Session=Depends(get_db)):

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
        return {"detail": "Team deleted"}