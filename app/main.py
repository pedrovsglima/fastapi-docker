from fastapi import FastAPI

from routers import team

app = FastAPI()

app.include_router(team.router)

@app.get("/")
def index() -> dict:
    return {"status": "OK"}
