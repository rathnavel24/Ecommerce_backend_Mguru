from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.app.Schemas.categories_schema import CategoryCreate,CategoryUpdate
from app.app.crud.category_crud import Category_Create,get_all_categories
from app.app.crud.category_crud import update_category,delete_category
from app.app.api.deps import get_db

router = APIRouter()

@router.get("/All")
async def get_category(db:Session= Depends(get_db)):
    return get_all_categories(db)

@router.post("/create")
async def create_new_category(data: CategoryCreate, db: Session= Depends(get_db)):
    return Category_Create(db,data)

@router.put("/update")
def update_category_api(
    categories_id : int,
    data: CategoryUpdate,
    db: Session = Depends(get_db)
):
    return update_category(db, categories_id, data)

@router.delete("/delete")
def delete_category_api(
    categories_id: int, db: Session= Depends(get_db)):

    return delete_category(db,categories_id)