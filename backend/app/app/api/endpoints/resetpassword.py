from fastapi import APIRouter, Depends
from app.app.Schemas.resetpassword_schema import ResetPassword
from app.app.crud.resetpassword_crud import reset_password 
from sqlalchemy.orm import Session
from app.app.crud.login_crud import LoginDetails
from app.app.api.deps import get_db


router=APIRouter()

@router.post("/reset-password")
def reset_user_password(data: ResetPassword, db: Session = Depends(get_db)):
    result = reset_password(db, data)
    return {"message": result}