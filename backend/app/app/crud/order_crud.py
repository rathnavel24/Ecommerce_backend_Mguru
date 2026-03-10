from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.app.models.ecommerce_order import EcommerceOrder
from app.app.models.ecomerce_useraddress import EcommerceUserAddress


from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.app.models.ecommerce_order import EcommerceOrder
from app.app.models.ecomerce_useraddress import EcommerceUserAddress


# USER - Create Order
def create_order(db: Session, order, user_id: int):

    address = db.query(EcommerceUserAddress).filter(
        EcommerceUserAddress.id == order.shipping_address,
        EcommerceUserAddress.user_id == user_id
    ).first()

    if not address:
        raise HTTPException(status_code=400, detail="Invalid address")

    new_order = EcommerceOrder(
        user_id=user_id,
        shipping_address=order.shipping_address,
        total_price=order.total_price,
        order_status="placed",
        status="active",
        created_by="user"
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order


# USER - Get My Orders
def get_user_orders(db: Session, user_id: int):

    return db.query(EcommerceOrder).filter(
        EcommerceOrder.user_id == user_id,
        EcommerceOrder.status == "active"
    ).all()


# USER - Get Single Order
def get_order(db: Session, order_id: int, user_id: int):

    order = db.query(EcommerceOrder).filter(
        EcommerceOrder.order_id == order_id,
        EcommerceOrder.user_id == user_id
    ).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order


# USER - Cancel Order
def cancel_order(db: Session, order_id: int, user_id: int):

    order = db.query(EcommerceOrder).filter(
        EcommerceOrder.order_id == order_id,
        EcommerceOrder.user_id == user_id
    ).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.order_status = "cancelled"

    db.commit()
    db.refresh(order)

    return order


# ADMIN - Get All Orders
def get_all_orders(db: Session):

    return db.query(EcommerceOrder).all()


# ADMIN - Update Order Status
def update_order_status(db: Session, order_id: int, status: str):

    order = db.query(EcommerceOrder).filter(
        EcommerceOrder.order_id == order_id
    ).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.order_status = status

    db.commit()
    db.refresh(order)

    return order