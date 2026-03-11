from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.app.api.deps import get_db
from app.app.api.deps import get_current_user

from app.app.Schemas.cart_schema import CartUpdate, CartRemove

from app.app.crud.cart_crud import CartDetails


router = APIRouter(prefix="/cart", tags=["Cart"])


# UPDATE CART (ADD OR UPDATE ITEMS)
@router.post("/update")
def update_cart(
    cart_data: CartUpdate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):

    return CartDetails(db).update_cart(
        user_id=user["user_id"],
        items=cart_data.items
    )


# GET USER CART
@router.get("/my-cart")
def get_cart(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):

    return CartDetails(db).get_cart(user["user_id"])


# REMOVE ITEMS FROM CART
@router.delete("/remove")
def remove_cart_items(
    remove_data: CartRemove,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):

    return CartDetails(db).remove_items(
        user_id=user["user_id"],
        product_ids=remove_data.product_ids
    )