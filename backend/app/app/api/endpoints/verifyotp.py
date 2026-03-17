from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.app.api.deps import get_db
from app.app.db.session import sessionLocal
from app.app.Schemas.verifyotp_schema import VerifyOtp
from app.app.crud.verifyotp_crud import VerifyOTPCRUD


router = APIRouter(tags=["login"])



@router.post("/verify_otp")
async def verify_otp(
    data: VerifyOtp,
    db: Session = Depends(get_db)
):
    try:
        return VerifyOTPCRUD(
            db,
            data.otp_key,
            data.otp
        ).verify()

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))