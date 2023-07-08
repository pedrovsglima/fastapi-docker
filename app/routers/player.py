from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter(prefix="/players", tags=["players"])

@router.get("/all", response_model=List[schemas.PlayerInfoResponse])
def list_all_players(db:Session=Depends(get_db)):

    result = (
        db.query(models.PlayerCareer)
        .distinct()
        .all()
    )

    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No players")


@router.get("/stats-per-game")
def stats_per_game(player:schemas.PlayerAndSeason, db:Session=Depends(get_db)):

    query_filter = [models.PlayerStatsPerGame.player_id==player.id]
    if player.season:
        query_filter.append(models.PlayerStatsPerGame.season==player.season)

    result = db.query(models.PlayerStatsPerGame).filter(*query_filter).all()

    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No player has the id {player.id}")


@router.get("/totals")
def stats_per_game(player:schemas.PlayerAndSeason, db:Session=Depends(get_db)):

    query_filter = [models.PlayerTotal.player_id==player.id]
    if player.season:
        query_filter.append(models.PlayerTotal.season==player.season)

    result = db.query(models.PlayerTotal).filter(*query_filter).all()

    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No player has the id {player.id}")


@router.get("/season")
def season_info(player:schemas.PlayerAndSeason, db:Session=Depends(get_db)):

    query_filter = [models.PlayerSeasonInfo.player_id==player.id]
    if player.season:
        query_filter.append(models.PlayerSeasonInfo.season==player.season)

    result = db.query(models.PlayerSeasonInfo).filter(*query_filter).all()

    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No player has the id {player.id}")


@router.get("/{player_id}", response_model=schemas.PlayerInfoResponse)
def query_player_by_id(player_id:int, db:Session=Depends(get_db)):

    result = (
        db.query(models.PlayerCareer)
        .filter(models.PlayerCareer.player_id==player_id)
        .first()
    )

    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No player has the id {player_id}")