from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.app.api.deps import get_db, role_required
from app.app.Schemas.checkout_schema import CheckoutRequest
from app.app.crud.order_service import CheckoutService

router = APIRouter(prefix="/checkout", tags=["Checkout"])


@router.post("/")
def checkout(
    data: CheckoutRequest,
    db: Session = Depends(get_db),
    user = Depends(role_required(["user", "admin", "merchant"]))
):

    return CheckoutService(db).checkout(
        user_id=user["user_id"],
        address_id=data.shipping_address
    )