from fastapi import APIRouter,Depends
from app.app.Schemas.usersignup_schema import UserSignUp
from sqlalchemy.orm import Session
from app.app.crud.signup_crud import SignUpDetails
from app.app.api.deps import get_db
router = APIRouter()

@router.post("/signup")
async def signup(user_data:UserSignUp,db:Session =  Depends(get_db)):
        try :
            return SignUpDetails(db,user_data).user_signup()
        except Exception as e:
             return e