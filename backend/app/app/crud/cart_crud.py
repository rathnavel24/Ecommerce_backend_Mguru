from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.app.models.ecommerce_cart import EcommerceCart
from app.app.models.ecommerce_inventory import EcommerceInventory
from app.app.models.ecommerce_productinfo import EcommerceProductInfo


class CartDetails:

    def __init__(self, db: Session):
        self.db = db


    def update_cart(self, user_id: int, items: list):

        updated_cart = []

        for item in items:

            product = self.db.query(EcommerceProductInfo).filter(
                EcommerceProductInfo.product_id == item.product_id,
                EcommerceProductInfo.status == "active"
            ).first()

            if not product:
                raise HTTPException(404, "Product not found")

            inventory = self.db.query(EcommerceInventory).filter(
                EcommerceInventory.product_id == item.product_id
            ).first()

            if not inventory:
                raise HTTPException(404, "Inventory not found")

            cart_item = self.db.query(EcommerceCart).filter(
                EcommerceCart.user_id == user_id,
                EcommerceCart.product_id == item.product_id
            ).first()

            previous_qty = 0

            if cart_item:
                previous_qty = cart_item.quantity
                cart_item.quantity = item.quantity
                cart_item.total_price = item.quantity * product.price
            else:
                cart_item = EcommerceCart(
                    user_id=user_id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    total_price=item.quantity * product.price,
                    status="active",
                    createdby="user"
                )
                self.db.add(cart_item)

            # adjust reserved inventory
            diff = item.quantity - previous_qty

            if inventory.stock_quantity - inventory.reserved_quantity < diff:
                raise HTTPException(
                    400,
                    f"Insufficient stock for {product.product_name}"
                )

            inventory.reserved_quantity += diff

            updated_cart.append(cart_item)

        self.db.commit()

        return updated_cart
    def remove_items(self, user_id: int, product_ids: list):

        for pid in product_ids:

            cart_item = self.db.query(EcommerceCart).filter(
                EcommerceCart.user_id == user_id,
                EcommerceCart.product_id == pid
            ).first()

            if not cart_item:
                continue

            inventory = self.db.query(EcommerceInventory).filter(
                EcommerceInventory.product_id == pid
            ).first()

            inventory.reserved_quantity -= cart_item.quantity

            self.db.delete(cart_item)

        self.db.commit()

        return {"message": "Items removed"}