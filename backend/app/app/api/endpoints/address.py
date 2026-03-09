from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.app.api.deps import get_db
from app.app.Schemas.address_schema import CreateAddress,UpdateAddress
from app.app.crud import address_crud
from app.app.crud.address_crud import delete_address

router = APIRouter(prefix="/address", tags=["Address"])



@router.get("/")
def get_addresses(db: Session = Depends(get_db)):
    return address_crud.get_addresses(db)

@router.post("/create")
def create_address(
    data: CreateAddress, 
    db: Session = Depends(get_db)
):
    return address_crud.create_address(db, data)


@router.get("/{user_id}")
def get_address(
    user_id: int, 
    db: Session = Depends(get_db)
):
    return address_crud.get_user_by_id(db, user_id)

@router.put("/update")
def update_user_address(
    user_id: int, 
    data: UpdateAddress, 
    db: Session = Depends(get_db)
):
    return address_crud.update_address(db,user_id,data)

@router.delete("/delete")
def delete_user_address(
    user_id:int, 
    db: Session= Depends(get_db)
):
    return delete_address(db,user_id)