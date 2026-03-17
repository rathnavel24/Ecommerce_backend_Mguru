from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette import status
from app.app.models.ecommerce_order import EcommerceOrder
from app.app.models.ecommerce_orderitems import EcommerceOrderItems
from app.app.models.ecommerce_inventory import EcommerceInventory

class BuyNow():
    def __init__(self,db : Session,data):
        self.db = db
        self.data = data
    
    def buynow(self,id):

        order_item = self.data.product_id
        quantity = self.data.quantity
        user_id = id

        inventory = self.db.query(EcommerceInventory).filter(EcommerceInventory.product_id == order_item).first()

        if not inventory :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No product available in this name")
        
        if quantity > inventory.stock_quantity :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No stock available")
        
        inventory.stock_quantity -= quantity

        product = inventory.product

        discounted_price = product.price - (
                product.price * product.discount_percent / 100
            )
        order = EcommerceOrder(
            user_id=user_id,
            shipping_address=self.data.address_id,
            total_price=discounted_price,
            order_status="placed",
            status="active",
            created_by="system"
        )

        self.db.add(order)
        self.db.flush()

        order_items = EcommerceOrderItems(
                order_id=order.order_id,
                product_id=order_item,
                product_name=product.product_name,
                price=discounted_price,
                quantity=quantity,
                status="active",
                createdby="system"
        )
        self.db.add(order_items)

        self.db.commit()

        return {
            "msg" : "order placed successfully"
        }