from fastapi import APIRouter,Depends
from app.app.Schemas.userlogin_schema import UserLogin
from sqlalchemy.orm import Session
from app.app.crud.login_crud import LoginDetails
from app.app.api.deps import get_db
router = APIRouter()

@router.post("/login")
async def login(user_data:UserLogin,db:Session =  Depends(get_db)):
        try :
            return LoginDetails(db,user_data).user_validation()
        except Exception as e:
             raise e