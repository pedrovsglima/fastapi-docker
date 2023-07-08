from fastapi import FastAPI

from routers import team, player

app = FastAPI()

routers = [
    team.router,
    player.router,
]
for router in routers:
    app.include_router(router)

@app.get("/")
def index() -> dict:
    return {"status": "OK"}
