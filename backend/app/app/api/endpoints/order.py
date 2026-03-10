from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.app.api.deps import get_db, get_current_user
from app.app.crud import order_crud
from app.app.Schemas.order_schema import OrderCreate, OrderStatusUpdate


router = APIRouter(prefix="/orders", tags=["Orders"])



# USER APIs

# User - Create Order
@router.post("/user")
def create_order(order: OrderCreate,
                 db: Session = Depends(get_db),
                 current_user = Depends(get_current_user)):

    user_id = current_user["user_id"]

    return order_crud.create_order(db, order, user_id)


# User - Get My Orders
@router.get("/user/my")
def get_my_orders(db: Session = Depends(get_db),
                  current_user = Depends(get_current_user)):

    user_id = current_user["user_id"]

    return order_crud.get_user_orders(db, user_id)


# User - Get Single Order
@router.get("/user/{order_id}")
def get_order(order_id: int,
              db: Session = Depends(get_db),
              current_user = Depends(get_current_user)):

    user_id = current_user["user_id"]

    return order_crud.get_order(db, order_id, user_id)


# User - Cancel Order
@router.put("/user/{order_id}/cancel")
def cancel_order(order_id: int,
                 db: Session = Depends(get_db),
                 current_user = Depends(get_current_user)):

    user_id = current_user["user_id"]

    return order_crud.cancel_order(db, order_id, user_id)



# ADMIN APIs
# Admin - Get All Orders
@router.get("/admin/all")
def get_all_orders(db: Session = Depends(get_db),
                   current_user = Depends(get_current_user)):

    if current_user["type"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    return order_crud.get_all_orders(db)


# Admin - Update Order Status
@router.put("/admin/{order_id}")
def update_order_status(order_id: int,
                        status: OrderStatusUpdate,
                        db: Session = Depends(get_db),
                        current_user = Depends(get_current_user)):

    if current_user["type"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    return order_crud.update_order_status(db, order_id, status.order_status)