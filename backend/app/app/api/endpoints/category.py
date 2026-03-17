from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlalchemy.orm import Session
from app.app.Schemas.categories_schema import CategoryCreate, CategoryUpdate
from app.app.crud.category_crud import (Category_Create,get_all_categories,
                                        update_category,delete_category)
from app.app.api.deps import get_db
from app.app.api.deps import get_current_user
from app.app.api.deps import role_required
from app.app.crud.image_services import upload_image

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
    category_name: str = Form(...),
    status: str = Form("active"),
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    user = Depends(role_required(["admin"]))
):
    
    image_url = upload_image(image)

    data = CategoryCreate(
        name=category_name,
        status=status,
        image_url=image_url
    )

    user_id = user.get("user_id")

    return Category_Create(db, data, user_id)


# UPDATE CATEGORY (ADMIN ONLY)
@router.put("/update/{category_id}")
def update_category_api(
    category_id: int,

    name: str = Form(None),
    parent_id: int = Form(None),
    status: str = Form(None),

    image: UploadFile = File(None),
    image_url: str = Form(None),

    db: Session = Depends(get_db),
    user=Depends(role_required(["admin"]))
):

    data = CategoryUpdate(
        name=name,
        parent_id=parent_id,
        status=status
    )

    return update_category(db, category_id, data, image, image_url)

# DELETE CATEGORY (ADMIN ONLY)
@router.delete("/delete")
def delete_category_api(
    categories_id: int,
    db: Session = Depends(get_db),
    user = Depends(role_required(["admin"]))
):
    return delete_category(db, categories_id)