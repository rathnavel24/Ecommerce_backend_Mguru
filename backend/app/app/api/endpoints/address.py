# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session

# from app.app.api.deps import get_db
# from app.app.Schemas.address_schema import CreateAddress
# from app.app.crud import address_crud

# router = APIRouter(prefix="/address", tags=["Address"])


# @router.post("/create")
# def create_address(data: CreateAddress, db: Session = Depends(get_db)):
#     return address_crud.create_address(db, data)


# @router.get("/")
# def get_addresses(db: Session = Depends(get_db)):
#     return address_crud.get_addresses(db)


# @router.get("/{address_id}")
# def get_address(address_id: int, db: Session = Depends(get_db)):
#     return address_crud.get_address_by_id(db, address_id)