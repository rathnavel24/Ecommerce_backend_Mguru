from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.app.Schemas.categories_schema import CategoryCreate, CategoryUpdate
from app.app.crud.category_crud import (Category_Create,get_all_categories,
                                        update_category,delete_category)
from app.app.api.deps import get_db
from app.app.api.deps import get_current_user
from app.app.api.deps import role_required

router = APIRouter(prefix="/category", tags=["Category"])


# GET ALL CATEGORIES (Public / Any logged user)
@router.get("/all")
async def get_category(
    db: Session = Depends(get_db)
):
    return get_all_categories(db)


# CREATE CATEGORY (ADMIN ONLY)
@router.post("/create")
async def create_new_category(
    data: CategoryCreate,
    db: Session = Depends(get_db),
    user = Depends(role_required(["admin"]))
):
    user_id = user.get("user_id")
    return Category_Create(db, data,user_id)


# UPDATE CATEGORY (ADMIN ONLY)
@router.put("/update")
def update_category_api(
    categories_id: int,
    data: CategoryUpdate,
    db: Session = Depends(get_db),
    user = Depends(role_required(["admin"]))
):
    return update_category(db, categories_id, data)


# DELETE CATEGORY (ADMIN ONLY)
@router.delete("/delete")
def delete_category_api(
    categories_id: int,
    db: Session = Depends(get_db),
    user = Depends(role_required(["admin"]))
):
    return delete_category(db, categories_id)