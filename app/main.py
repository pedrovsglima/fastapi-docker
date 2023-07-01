from csv import DictReader
from fastapi import FastAPI

from .routers import team

app = FastAPI()

with open("./nba-stats/team-summaries.csv","r") as f:
    teams = list(DictReader(f))

app.include_router(team.router)


@app.get("/")
def index() -> dict:
    return {"status": "OK"}
