from sqlalchemy.orm import Session
from app.app.models.ecommerce_categories import EcommerceCategories
from app.app.Schemas.categories_schema import CategoryCreate, CategoryUpdate
from  fastapi import HTTPException


def Category_Create(db: Session, category: CategoryCreate,user_id):

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
        created_by=str(user_id)
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category

def get_all_categories(db:Session):
    category =db.query(EcommerceCategories).all()
    return category

def update_category(db: Session, category_id: int, data: CategoryUpdate):
    category = db.query(EcommerceCategories).filter(EcommerceCategories.categories_id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    if data.name is not None:
        category.name = data.name

    if data.parent_id is not None:
        parent = db.query(EcommerceCategories).filter(
            EcommerceCategories.categories_id == data.parent_id
        ).first()

        if not parent:
            raise HTTPException(status_code=400, detail="Parent category not found")

        category.parent_id = data.parent_id

    db.commit()
    db.refresh(category)
        
    return category
    
def delete_category(db:Session, category_id : int):

    category = db.query(EcommerceCategories).filter(EcommerceCategories.categories_id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    category.status = "deleted"
    
    db.commit()
    db.refresh(category)

    return {"message" : "Category Deleted Successfully"}
    





