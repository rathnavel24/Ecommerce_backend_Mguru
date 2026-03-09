<<<<<<< HEAD
=======
from sqlalchemy.orm import Session
from app.app.models.ecomerce_useraddress import EcommerceUserAddress
from app.app.Schemas.address_schema import UpdateAddress
from app.app.models.ecommerce_user import Users
from fastapi import HTTPException

def create_address(db: Session, data):
    address = EcommerceUserAddress(
        user_id=data.user_id,
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


def get_addresses(db: Session):
    return db.query(EcommerceUserAddress).all()


def get_user_by_id(db: Session, user_id: int):
    address = db.query(EcommerceUserAddress).filter(
        EcommerceUserAddress.user_id == user_id
    ).first()
    if not address:
        raise HTTPException(status_code=404, detail="User not found")
    db.commit()
    db.refresh(address)
    return address


def update_address(db:Session, user_id:int, data:UpdateAddress):
    user_address = db.query(EcommerceUserAddress).filter(EcommerceUserAddress.user_id == user_id).first()
    if not user_address:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_address.address_line1 = data.address_line1
    user_address.address_line2 = data.address_line2
    user_address.city = data.city
    user_address.state = data.state
    user_address.country = data.country
    user_address.pincode = data.pincode
    user_address.isdefault = data.isdefault

    db.commit()
    db.refresh(user_address)
    return user_address

       

def delete_address(db:Session, user_id:int):
    user_address = db.query(EcommerceUserAddress).filter(
        EcommerceUserAddress.user_id == user_id
    ).first()
    if not user_address:
        raise HTTPException(status_code=404, detail="address not found")
    user_address.status = "deleted"
    
    db.delete(user_address)
    db.commit()
    return "User address deleted successfully"
    
        
    
    






>>>>>>> 1e523646ff603304c3a651b7fe30499a6a72c79f
