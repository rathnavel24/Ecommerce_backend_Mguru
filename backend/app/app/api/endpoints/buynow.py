from typing import Annotated

from fastapi import APIRouter ,Depends
from sqlalchemy.orm import Session
from app.app.api.deps import get_db
from app.app.api.deps import get_current_user
from app.app.api.deps import role_required
from app.app.Schemas.order_schema import OrderBuyNow

from app.app.crud.buynow_crud import BuyNow


router = APIRouter(tags=["Orders"])

@router.post("/buynow")
async def buynow(db :Annotated[Session,Depends(get_db)], user : Annotated[str,Depends(role_required(['user']))],data: OrderBuyNow):
    
    return BuyNow(db,data).buynow(user.get("user_id"))