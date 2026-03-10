from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.app.api.deps import get_db
<<<<<<< HEAD
=======
from app.app.db.session import sessionLocal
from app.app.crud.login_crud import LoginUser
from app.app.Schemas.userlogin_schema import UserLogin
>>>>>>> 647d57c7e93122d907efcae0a4babf021094a3bf

router = APIRouter()



@router.post("/login")
async def login(data: UserLogin, db: Session = Depends(get_db)):

    return LoginUser(db, data.email, data.password).login()