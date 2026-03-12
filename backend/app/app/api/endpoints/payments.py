from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.app.Schemas.payment_schema import PaymentCreate, PaymentUpdate
from app.app.crud.payment_crud import PaymentsDetails
from app.app.api.deps import get_db
from app.app.api.deps import role_required


router = APIRouter(prefix="/payment", tags=["Payments"])

# GET PAYMENTS (ADMIN + MERCHANT)
@router.get("/all-payments")
async def get_payments(
    db: Session = Depends(get_db),
    user=Depends(role_required(["admin", "merchant"]))
):
    try:
        return PaymentsDetails(db, None).get_all_payments()
    except Exception as e:
        raise e
    


# CREATE PAYMENT (USER)
@router.post("/create")
async def create_payment(
    payment_data : PaymentCreate,
    db: Session = Depends(get_db), 
    user = Depends(role_required(["user"]))  
):
    try:
        return PaymentsDetails(db, payment_data).create_payment()
    
    except Exception as e:
        raise e
    


# UPDATE PAYMENT (ADMIN + MERCHANT)
@router.put("/update")
async def update_payment(
    payment_id : int,
    payment_data : PaymentUpdate,
    db: Session = Depends(get_db),
    user = Depends(role_required(["admin" , "merchant"]))
):
    try:
        return PaymentsDetails(db, payment_data).update_payment(payment_id)
    except Exception as e:
        raise e

