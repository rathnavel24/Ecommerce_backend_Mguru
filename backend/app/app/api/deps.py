from app.app.db.session import sessionLocal
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError

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

<<<<<<< HEAD
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
=======
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
>>>>>>> 83e2f83e46b573eae6fda581dcdc2cee25e18db3
