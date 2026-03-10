from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.app.api.deps import get_db, get_current_user
from app.app.Schemas.address_schema import CreateAddress, UpdateAddress
from app.app.crud import address_crud

router = APIRouter(prefix="/address", tags=["Address"])


# CREATE ADDRESS
@router.post("/create")
def create_address(
    data: CreateAddress,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    user_id = current_user["user_id"]

    return address_crud.create_address(db, data, user_id)


# GET MY ADDRESSES
@router.get("/my")
def get_my_addresses(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    user_id = current_user["user_id"]

    return address_crud.get_user_by_id(db, user_id)


# UPDATE ADDRESS
@router.put("/update")
def update_address(
    data: UpdateAddress,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    user_id = current_user["user_id"]

    return address_crud.update_address(db, user_id, data)


# DELETE ADDRESS
@router.delete("/delete")
def delete_address(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    user_id = current_user["user_id"]

    return address_crud.delete_address(db, user_id)