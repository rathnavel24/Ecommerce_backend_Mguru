from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.app.api.deps import get_db, role_required
from app.app.crud.order_items_crud import OrderItemsDetails


router = APIRouter(
    prefix="/order-items",
    tags=["Order Items"]
)


# ADMIN - VIEW ALL ORDER ITEMS
@router.get("/all")
def get_all_order_items(
    db: Session = Depends(get_db),
    user=Depends(role_required(["admin"]))
):

    return OrderItemsDetails(db).get_all_order_items()



# USER - VIEW ORDER ITEMS
@router.get("/{order_id}")
def get_order_items(
    order_id: int,
    db: Session = Depends(get_db),
    user=Depends(role_required(["user"]))
):

    return OrderItemsDetails(db).get_order_items(
        order_id,
        user["user_id"]
    )


