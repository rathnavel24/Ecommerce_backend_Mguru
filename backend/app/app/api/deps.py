from app.app.db.session import sessionLocal
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt

def get_db():
    db = sessionLocal()
    try :
        yield db
    finally:
        db.close()



security = HTTPBearer()

SECRET_KEY = "MqbU2rs3hlCKUWrt3ZvTeg7NxVTgTBPlJkRLWLpgoDttc8IG6I0NTzDwwzJsk"
ALGORITHM = "HS256"


def get_current_user(token=Depends(security)):

    try:
        payload = jwt.decode(
            token.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")