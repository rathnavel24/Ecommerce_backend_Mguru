from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.app.api.deps import get_db
from app.app.Schemas.address_schema import CreateAddress, UpdateAddress
from app.app.crud.address_crud import (create_address,get_addresses,get_user_by_id,
                                       update_address,delete_address)
from app.app.api.deps import get_current_user
from app.app.api.deps import role_required


router = APIRouter(prefix="/address", tags=["Address"])


# CREATE ADDRESS (USER ONLY)
@router.post("/create_address")
def create_user_address(data: CreateAddress,db: Session = Depends(get_db),user=Depends(role_required(["user"]))):
    return create_address(db, data, user["user_id"])


# GET ALL ADDRESSES (ADMIN ONLY)
@router.get("/all")
def get_all_addresses(db: Session = Depends(get_db),user=Depends(role_required(["admin"]))):
    return get_addresses(db)


# GET CURRENT USER ADDRESSES
@router.get("/my")
def get_my_addresses(db: Session = Depends(get_db),user=Depends(role_required(["user"]))):
    return get_user_by_id(db, user["user_id"])


# UPDATE ADDRESS
@router.put("/update/{address_id}")
def update_user_address(address_id: int, data: UpdateAddress, db:Session = Depends(get_db),user=Depends(role_required(["user"]))):
    return update_address(db, address_id, user["user_id"], data)


# DELETE ADDRESS
@router.delete("/")
def delete_user_address(db: Session = Depends(get_db),user=Depends(role_required(["user"]))):
    return delete_address(db, user["user_id"])