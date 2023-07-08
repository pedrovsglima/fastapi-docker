from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter(prefix="/players", tags=["players"])

@router.get("/all", response_model=List[schemas.PlayerInfoResponse])
def list_all_players(db:Session=Depends(get_db)) -> dict:

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


@router.get("/{player_id}", response_model=schemas.PlayerInfoResponse)
def query_player_by_id(player_id:int, db:Session=Depends(get_db)) -> dict:

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

# TODO: get
# season-info (filtrar por player_id e season)
# player-per-game (filtrar por player_id, retornar todas as stats)
# player-totals (filtrar por player_id, retornar todas as stats)