from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.app.db.session import sessionLocal
from app.app.Schemas.forgot_password_schema import ForgotPassword
from app.app.crud.forgot_password_crud import ForgotPasswordCRUD

router = APIRouter()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/forgot-password")
async def forgot_password(data: ForgotPassword, db: Session = Depends(get_db)):

    try:
        return ForgotPasswordCRUD(db, data.email).send_otp()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))