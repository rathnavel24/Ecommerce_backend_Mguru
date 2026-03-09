# from sqlalchemy.orm import Session
# from app.app.models.ecommerce_order import EcommerceOrder

# def create_order(db: Session, data):

#     order = EcommerceOrder(
#         user_id = data.user_id,
#         total_price = data.total_price,
#         shipping_address= data.shipping_address

#     )

#     db.add(order)
#     db.commit()
#     db.refresh(order)

#     return order

# def get_orders(db: Session):
#     return db.query(EcommerceOrder).all()


# def get_order_by_id(db: Session, order_id: int):
#     return db.query(EcommerceOrder).filter(
#         EcommerceOrder.order_id == order_id
    # ).first()