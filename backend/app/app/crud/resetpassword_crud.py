# resetting password
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.app.Schemas import resetpassword_schema
from pydantic import BaseModel
from jose import jwt, JWTError
from passlib.context import CryptContext
from app.app.core.security import verify_password, get_password_hash
from app.app.api.deps import get_db
from app.app.models.ecommerce_user import Users
from app.app import models

def reset_password(db: Session, data):

    user = db.query(Users).filter(or_(
        Users.user_id == data.user_id,
        Users.email == data.email
    )).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    if not verify_password(data.existing_password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect existing password"
        )

    user.password = get_password_hash(data.new_password)

    db.commit()

    return "Password updated successfully"
     
    