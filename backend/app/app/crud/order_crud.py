from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.app.models.ecommerce_order import EcommerceOrder
from app.app.models.ecomerce_useraddress import EcommerceUserAddress


class OrderDetails:

    def __init__(self, db: Session):
        self.db = db


    # USER - Create Order
    def create_order(self, order, user_id: int, role: str):

        if role != "user":
            raise HTTPException(status_code=403, detail="Only user can create order")

        address = self.db.query(EcommerceUserAddress).filter(
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

        self.db.add(new_order)
        self.db.commit()
        self.db.refresh(new_order)

        return new_order


    # USER - Get Own Orders
    def get_user_orders(self, user_id: int, role: str):

        if role != "user":
            raise HTTPException(status_code=403, detail="Only user can view own orders")

        return self.db.query(EcommerceOrder).filter(
            EcommerceOrder.user_id == user_id,
            EcommerceOrder.status == "active"
        ).all()


    # USER - Get Single Order
    def get_order(self, order_id: int, user_id: int, role: str):

        if role != "user":
            raise HTTPException(status_code=403, detail="Only user can view this order")

        order = self.db.query(EcommerceOrder).filter(
            EcommerceOrder.order_id == order_id,
            EcommerceOrder.user_id == user_id
        ).first()

        if not order:
            raise HTTPException(status_code=404, detail="Order not found")

        return order


    # USER - Cancel Order
    def cancel_order(self, order_id: int, user_id: int, role: str):

        if role != "user":
            raise HTTPException(status_code=403, detail="Only user can cancel order")

        order = self.db.query(EcommerceOrder).filter(
            EcommerceOrder.order_id == order_id,
            EcommerceOrder.user_id == user_id
        ).first()

        if not order:
            raise HTTPException(status_code=404, detail="Order not found")

        if order.order_status in ["cancelled", "delivered"]:
            raise HTTPException(
                status_code=400,
                detail=f"Cannot cancel order with status {order.order_status}"
            )

        order.order_status = "cancelled"

        self.db.commit()
        self.db.refresh(order)

        return order


    # ADMIN - Get All Orders
    def get_all_orders(self, role: str):

        if role != "admin":
            raise HTTPException(status_code=403, detail="Admin access required")

        return self.db.query(EcommerceOrder).all()


    # ADMIN / MERCHANT - Update Order Status
    def update_order_status(self, order_id: int, status: str, role: str):

        if role not in ["admin", "merchant"]:
            raise HTTPException(
                status_code=403,
                detail="Admin or Merchant access required"
            )

        order = self.db.query(EcommerceOrder).filter(
            EcommerceOrder.order_id == order_id
        ).first()

        if not order:
            raise HTTPException(status_code=404, detail="Order not found")

        allowed_status = ["placed", "shipped", "delivered", "cancelled"]

        if status not in allowed_status:
            raise HTTPException(status_code=400, detail="Invalid order status")

        order.order_status = status

        self.db.commit()
        self.db.refresh(order)

        return order