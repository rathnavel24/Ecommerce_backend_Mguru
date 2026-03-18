from fastapi import APIRouter, Depends, HTTPException,BackgroundTasks
from sqlalchemy.orm import Session
from app.app.api.deps import get_db
from app.app.db.session import sessionLocal
from app.app.Schemas.resend_otp_schema import ResendOTP
from app.app.crud.resend_otp_crud import ResendOTPCRUD

router = APIRouter(tags=["login"])


@router.post("/resend_otp")
async def resend_otp(data: ResendOTP,background_tasks: BackgroundTasks, db: Session = Depends(get_db)):

    try:
        return ResendOTPCRUD(db, data.reset_key).resend(background_tasks)
    

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))