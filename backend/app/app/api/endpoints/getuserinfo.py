from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.app.db.session import sessionLocal
from app.app.crud.getuserinfo_crud import GetUserInfo
from app.app.api.deps import get_current_user
from app.app.api.deps import get_db

router = APIRouter()



@router.post("/get_user_info")
async def get_user_info(user=Depends(get_current_user),
                          db: Session = Depends(get_db)):
    try:
        return GetUserInfo(db,user['user_id']).getuserinfo()
    except Exception as e:
        return e