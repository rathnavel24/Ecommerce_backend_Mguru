from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.app.api.deps import get_db
from app.app.Schemas.order_schema import CreateOrder
from app.app.crud import order_crud

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/create")
def create_order(data: CreateOrder, db: Session = Depends(get_db)):
    return order_crud.create_order(db, data)


@router.get("/")
def get_orders(db: Session = Depends(get_db)):
    return order_crud.get_orders(db)


@router.get("/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    return order_crud.get_order_by_id(db, order_id)