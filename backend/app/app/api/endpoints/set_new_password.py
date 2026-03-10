from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.app.db.session import sessionLocal
from app.app.Schemas.set_new_password_schema import SetNewPassword
from app.app.crud.set_new_password_crud import SetNewPasswordCRUD
from app.app.api.deps import get_db

router = APIRouter()



@router.post("/set_new_password")
async def set_new_password(data: SetNewPassword, db: Session = Depends(get_db)):
    try:
        return SetNewPasswordCRUD(
            db,
            data.otp_key,
            data.new_password
        ).reset()

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))