from fastapi import APIRouter, Depends,BackgroundTasks
from sqlalchemy.orm import Session
from app.app.api.deps import get_db
from app.app.db.session import sessionLocal
from app.app.crud.login_crud import LoginUser
from app.app.Schemas.userlogin_schema import UserLogin



router = APIRouter(tags=["login"])


@router.post("/login")
async def login(data: UserLogin,background_tasks: BackgroundTasks, db: Session = Depends(get_db)):

    return LoginUser(db, data.email, data.password).login(background_tasks)