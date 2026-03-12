from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.app.api.deps import get_db, role_required
from app.app.Schemas.order_schema import OrderCreate, OrderStatusUpdate
from app.app.crud.order_crud import OrderDetails

router = APIRouter(prefix="/orders", tags=["Orders"])


# USER - CREATE ORDER
@router.post("/")
def create_user_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    user=Depends(role_required(["user"]))
):
    order_service = OrderDetails(db)

    return order_service.create_order(
        order,
        user["user_id"],
        user["role"]
    )


# USER - GET MY ORDERS
@router.get("/my")
def get_my_orders(
    db: Session = Depends(get_db),
    user=Depends(role_required(["user","admin"]))
):
    order_service = OrderDetails(db)

    return order_service.get_user_orders(
        user["user_id"],
        user["role"]
    )


# ADMIN - GET ALL ORDERS (MOVE THIS ABOVE)
@router.get("/all")
def get_all_orders(
    db: Session = Depends(get_db),
    user=Depends(role_required(["admin"]))
):
    order_service = OrderDetails(db)

    return order_service.get_all_orders(
        user["role"]
    )


# USER - GET SINGLE ORDER
@router.get("/{order_id}")
def get_single_order(
    order_id: int,
    db: Session = Depends(get_db),
    user=Depends(role_required(["user"]))
):
    order_service = OrderDetails(db)

    return order_service.get_order(
        order_id,
        user["user_id"],
        user["role"]
    )


# USER - CANCEL ORDER
@router.put("/cancel/{order_id}")
def cancel_user_order(
    order_id: int,
    db: Session = Depends(get_db),
    user=Depends(role_required(["user"]))
):
    order_service = OrderDetails(db)

    return order_service.cancel_order(
        order_id,
        user["user_id"],
        user["role"]
    )


# ADMIN / MERCHANT - UPDATE STATUS
@router.put("/status/{order_id}")
def update_order_status(
    order_id: int,
    db: Session = Depends(get_db),
    user=Depends(role_required(["admin", "merchant"]))
):
    order_service = OrderDetails(db)

    return order_service.update_order_status(
        order_id,
        user["role"]
    )