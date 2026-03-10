from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.app.db.session import sessionLocal
from app.app.Schemas.reset_password_schema import ResetPassword
from app.app.crud.reset_password_crud import ResetPasswordCRUD
from app.app.api.deps import get_db

router = APIRouter()

@router.post("/reset-password")
async def reset_password(data: ResetPassword, db: Session = Depends(get_db)):

    try:
        return ResetPasswordCRUD(
            db,
            data.reset_key,
            data.otp,
            data.new_password
        ).reset()

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))