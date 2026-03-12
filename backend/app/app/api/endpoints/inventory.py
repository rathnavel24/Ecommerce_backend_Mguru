from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.app.Schemas.inventory_schema import InventoryCreate, InventoryUpdate
from app.app.crud.inventory_crud import InventoryDetails
from app.app.api.deps import get_db
from app.app.api.deps import role_required


router = APIRouter(prefix="/inventory", tags=["Inventory"])


# GET INVENTORY PRODUCTS (ADMIN + MERCHANT)
@router.get("/all-products")
async def get_products_inven(
    db: Session = Depends(get_db),
    user=Depends(role_required(["admin", "merchant","user"]))
):
    try:
        return InventoryDetails(db, None).get_all_products_inven()
    except Exception as e:
        raise e


# CREATE INVENTORY (ADMIN + MERCHANT)
@router.post("/create")
async def create_inventory(
    inventory_data: InventoryCreate,
    db: Session = Depends(get_db),
    user=Depends(role_required(["admin", "merchant","user"]))
):
    try:
        return InventoryDetails(db, inventory_data).create_inventory()
    except Exception as e:
        raise e


# UPDATE INVENTORY (ADMIN + MERCHANT)
@router.put("/update")
async def update_inventory(
    inventory_id: int,
    inventory_data: InventoryUpdate,
    db: Session = Depends(get_db),
    user=Depends(role_required(["admin", "merchant"]))
):
    try:
        return InventoryDetails(db, inventory_data).update_inventory(inventory_id)
    except Exception as e:
        raise e


# DELETE INVENTORY (ADMIN ONLY)
@router.delete("/delete")
async def delete_inventory(
    inventory_id: int,
    db: Session = Depends(get_db),
    user=Depends(role_required(["admin","user"]))
):
    try:
        return InventoryDetails(db, None).delete_inventory(inventory_id)
    except Exception as e:
        raise e