from sqlalchemy.orm import Session
# from app.app.models.user_address import EcommerceUserAddress
# from app.app.models.user_address import EcommerceUserAddress

# def create_address(db: Session, data):
#     address = EcommerceUserAddress(
#         user_id=data.user_id,
#         address_line1=data.address_line1,
#         address_line2=data.address_line2,
#         city=data.city,
#         state=data.state,
#         country=data.country,
#         pincode=data.pincode,
#         isdefault=data.isdefault
#     )

#     db.add(address)
#     db.commit()
#     db.refresh(address)

#     return address


# def get_addresses(db: Session):
#     return db.query(EcommerceUserAddress).all()


# def get_address_by_id(db: Session, address_id: int):
#     return db.query(EcommerceUserAddress).filter(
#         EcommerceUserAddress.id == address_id
#     ).first()