from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.app.models.ecommerce_orderitems import EcommerceOrderItems
from app.app.models.ecommerce_order import EcommerceOrder
from app.app.models.ecommerce_productinfo import EcommerceProductInfo
from app.app.models.ecommerce_categories import EcommerceCategories


class OrderItemsDetails:

    def __init__(self, db: Session):
        self.db = db


    # USER - VIEW ITEMS OF THEIR ORDER
    def get_order_items(self, order_id: int, user_id: int):

        order = self.db.query(EcommerceOrder).filter(
            EcommerceOrder.order_id == order_id,
            EcommerceOrder.user_id == user_id
        ).first()

        if not order:
            raise HTTPException(status_code=404, detail="Order not found")

        items = (
            self.db.query(
                EcommerceOrderItems,
                EcommerceProductInfo.image_url,
                EcommerceCategories.name.label("category")
            )
            .join(
                EcommerceProductInfo,
                EcommerceOrderItems.product_id == EcommerceProductInfo.product_id
            )
            .join(
                EcommerceCategories,
                EcommerceProductInfo.categorie_id == EcommerceCategories.categories_id
            )
            .filter(EcommerceOrderItems.order_id == order_id)
            .all()
        )

        result = []

        for item, image_url, category in items:

            result.append({
                "orderitems_id": item.orderitems_id,
                "order_id": item.order_id,
                "product_id": item.product_id,
                "product_name": item.product_name,
                "image_url": image_url,
                "category": category,
                "price": item.price,
                "quantity": item.quantity,
                "total_price": item.price * item.quantity
            })

        return result


    # ADMIN - VIEW ALL ORDER ITEMS
    def get_all_order_items(self):

        items = (
            self.db.query(
                EcommerceOrderItems,
                EcommerceProductInfo.image_url,
                EcommerceCategories.name.label("category")
            )
            .join(
                EcommerceProductInfo,
                EcommerceOrderItems.product_id == EcommerceProductInfo.product_id
            )
            .join(
                EcommerceCategories,
                EcommerceProductInfo.categorie_id == EcommerceCategories.categories_id
            )
            .all()
        )

        result = []

        for item, image_url, category in items:

            result.append({
                "orderitems_id": item.orderitems_id,
                "order_id": item.order_id,
                "product_id": item.product_id,
                "product_name": item.product_name,
                "image_url": image_url,
                "category": category,
                "price": item.price,
                "quantity": item.quantity,
                "total_price": item.price * item.quantity
            })

        return result