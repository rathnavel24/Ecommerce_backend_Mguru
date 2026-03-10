from sqlalchemy.orm import Session
from app.app.models.ecomerce_useraddress import EcommerceUserAddress
from app.app.Schemas.address_schema import UpdateAddress
from fastapi import HTTPException


# CREATE ADDRESS
def create_address(db: Session, data, user_id: int):

    address = EcommerceUserAddress(
        user_id=user_id,
        address_line1=data.address_line1,
        address_line2=data.address_line2,
        city=data.city,
        state=data.state,
        country=data.country,
        pincode=data.pincode,
        isdefault=data.isdefault
    )

    db.add(address)
    db.commit()
    db.refresh(address)

    return address


# GET ALL ADDRESSES
def get_addresses(db: Session):
    return db.query(EcommerceUserAddress).all()


# GET USER ADDRESSES
def get_user_by_id(db: Session, user_id: int):

    addresses = db.query(EcommerceUserAddress).filter(
        EcommerceUserAddress.user_id == user_id
    ).all()

    if not addresses:
        raise HTTPException(status_code=404, detail="Address not found")

    return addresses


# UPDATE ADDRESS (PARTIAL UPDATE)
def update_address(db: Session, user_id: int, data: UpdateAddress):

    address = db.query(EcommerceUserAddress).filter(
        EcommerceUserAddress.user_id == user_id
    ).first()

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    update_data = data.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(address, key, value)

    db.commit()
    db.refresh(address)

    return address


# DELETE ADDRESS
def delete_address(db: Session, user_id: int):

    address = db.query(EcommerceUserAddress).filter(
        EcommerceUserAddress.user_id == user_id
    ).first()

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    
   
    db.delete(address)
    db.commit()

    return {"message": "User address deleted successfully"}