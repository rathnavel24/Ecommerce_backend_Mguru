from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.app.db.session import sessionLocal
from app.app.Schemas.change_password_schema import ChangePassword
from app.app.crud.change_password_crud import ChangePasswordCRUD
from app.app.api.deps import get_current_user
from app.app.api.deps import get_db

router = APIRouter()
router = APIRouter(tags=["login"])

@router.post("/change_password")
async def change_password(data: ChangePassword,user=Depends(get_current_user),
                          db: Session = Depends(get_db)):

    try:

        user_id = user["user_ id"]

        return ChangePasswordCRUD(
            db,
            user_id,
            data.old_password,
            data.new_password
        ).change()

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))