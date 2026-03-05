from fastapi import HTTPException
from passlib.context import CryptContext
from datetime import datetime as dt
from datetime import timedelta
from jose import ExpiredSignatureError, JWTError, jwt
from starlette import status
import random



pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def get_password_hash(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    """
    Verify if the plain password matches the hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)

SECRET_KEY = "MqbU2rs3hlCKUWrt3ZvTeg7NxVTgTBPlJkRLWLpgoDttc8IG6I0NTzDwwzJsk"
ALGORITHM = "HS256"
EXPIRE_MINUTES = 5

def create_token(data):
    user_token = {}
    user_token.update(data)
    expire = dt.now()+timedelta(minutes=EXPIRE_MINUTES)
    user_token.update({"exp":expire})
    return jwt.encode(user_token,SECRET_KEY,ALGORITHM)



def decode_token(token):
        try:
            payload = jwt.decode(token,algorithms=ALGORITHM,key=SECRET_KEY)
            return payload
        except ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Token has expired")
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid token")


def generate_otp():
    return str(random.randint(100000,999999))