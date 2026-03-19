from sqlalchemy.orm import Session
from app.app.models.ecommerce_categories import EcommerceCategories
from app.app.Schemas.categories_schema import CategoryCreate, CategoryUpdate
from  fastapi import File, HTTPException, UploadFile
from app.app.crud.image_services import upload_image

def Category_Create(db: Session, category: CategoryCreate, user_id):

    if category.parent_id is not None:
        parent = db.query(EcommerceCategories).filter(
            EcommerceCategories.categories_id == category.parent_id
        ).first()

        if not parent:
            raise HTTPException(status_code=400, detail="Parent category not found")

    new_category = EcommerceCategories(
        name=category.name,
        parent_id=category.parent_id,
        status=category.status,
        image_url=category.image_url,
        created_by=str(user_id)
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category

def get_all_categories(db:Session):
    category =db.query(EcommerceCategories).filter(EcommerceCategories.status == "active").all()
    return category


def update_category(db: Session,category_id: int,data: CategoryUpdate,image=None,image_url=None):

    category = db.query(EcommerceCategories)\
        .filter(EcommerceCategories.categories_id == category_id)\
        .first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    #  STRICT IMAGE LOGIC
    if image:
        category.image_url = upload_image(image)

    elif image_url:
        category.image_url = image_url

    else:
        raise HTTPException(
            status_code=400,
            detail="Image or image_url required"
        )

    # name update
    if data.name is not None:
        category.name = data.name

    # parent update
    if data.parent_id is not None:
        parent = db.query(EcommerceCategories)\
            .filter(EcommerceCategories.categories_id == data.parent_id)\
            .first()

        if not parent:
            raise HTTPException(status_code=400, detail="Parent category not found")

        category.parent_id = data.parent_id

    # status update
    if data.status is not None:
        category.status = data.status

    db.commit()
    db.refresh(category)

    return {"msg": "Category Updated Successfully"}

def delete_category(db:Session, category_id : int):

    category = db.query(EcommerceCategories).filter(EcommerceCategories.categories_id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    category.status = "deleted"
    
    db.commit()
    db.refresh(category)

    return {"message" : "Category Deleted Successfully"}
    





