from fastapi import APIRouter, Depends
from app.app.Schemas.forgotpassword_schema import ForgotPassword
from app.app.crud.forgotpassword_crud import forgot_password
from sqlalchemy.orm import Session
from app.app.crud.login_crud import LoginDetails
from app.app.api.deps import get_db

router = APIRouter()

@router.post("/forgot_password")
def forgot_user_password(user_data: ForgotPassword, db: Session = Depends(get_db)):
    return forgot_password(db, user_data.email)