from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.app.models.ecommerce_order import EcommerceOrder
from app.app.models.ecommerce_orderitems import EcommerceOrderItems
from app.app.models.ecommerce_cart import EcommerceCart
from app.app.models.ecommerce_inventory import EcommerceInventory
from app.app.models.ecommerce_productinfo import EcommerceProductInfo


class CheckoutService:

    def __init__(self, db: Session):
        self.db = db


    def checkout(self, user_id: int, address_id: int):

        cart_items = self.db.query(EcommerceCart).filter(
            EcommerceCart.user_id == user_id,
            EcommerceCart.status == "active"
        ).all()

        if not cart_items:
            raise HTTPException(status_code=400, detail="Cart empty")

        total_price = 0

        for item in cart_items:
            product = item.product

            discounted_price = product.price - (
                product.price * product.discount_percent / 100
            )

            total_price += discounted_price * item.quantity

    

        order = EcommerceOrder(
            user_id=user_id,
            shipping_address=address_id,
            total_price=total_price,
            order_status="placed",
            status="active",
            created_by="system"
        )

        self.db.add(order)
        self.db.flush()

        for item in cart_items:

            inventory = self.db.query(EcommerceInventory).filter(
                EcommerceInventory.product_id == item.product_id
            ).with_for_update().first()

            if inventory.stock_quantity < item.quantity:
                raise HTTPException(400, "Stock not available")

            inventory.stock_quantity -= item.quantity
            inventory.reserved_quantity -= item.quantity

            discounted_price = item.product.price - (
                item.product.price * item.product.discount_percent / 100
            )

            order_item = EcommerceOrderItems(
                order_id=order.order_id,
                product_id=item.product_id,
                product_name=item.product.product_name,
                price=discounted_price,
                quantity=item.quantity,
                status="active",
                createdby="system"
            )

            self.db.add(order_item)

        # clear cart
        for item in cart_items:
            self.db.delete(item)

        self.db.commit()

        return {
            "msg" : "order placed successfully"
        }