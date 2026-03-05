from fastapi import APIRouter,Depends
from app.app.Schemas.userlogin_schema import UserLogin
from sqlalchemy.orm import Session
from app.app.crud.getuserinfo_crud import GetUserInfo
from app.app.api.deps import get_db
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
router = APIRouter()

@router.get("/getuserinfo")
async def getuserinfo(token: str = Depends(oauth2_scheme),db:Session =  Depends(get_db)):
        try :
            return GetUserInfo(db,token).getuserinfo()
        except Exception as e:
             raise e