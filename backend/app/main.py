from app.app.db.init_db import init_db
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def test():
    
    return "Success"

init_db()