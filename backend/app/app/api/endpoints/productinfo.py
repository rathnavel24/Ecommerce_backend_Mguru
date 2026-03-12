from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.app.Schemas.productinfo_schema import ProductCreate
from app.app.crud.productinfo_crud import ProductDetails
from app.app.api.deps import get_db
from app.app.api.deps import get_current_user
from app.app.api.deps import role_required
router = APIRouter(prefix="/products", tags=["Products"])


# GET ALL PRODUCTS (PUBLIC / ANY USER)
@router.get("/all_products")
async def get_products(db: Session = Depends(get_db)):
    try:
        return ProductDetails(db, None).get_all_products()
    except Exception as e:
        raise e

@router.get("/products/category/{category_id}")
def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    return ProductDetails(db, None).get_products_by_category(category_id)

    
# CREATE PRODUCT (ADMIN + MERCHANT)
@router.post("/create_product")
async def create_product(
    product_data: ProductCreate,
    db: Session = Depends(get_db),
    user=Depends(role_required(["admin", "merchant"])),
    user_id=Depends(get_current_user)
):
    try:
        return ProductDetails(db, product_data).create_product(user_id.get("role"))
    except Exception as e:
        raise e


# UPDATE PRODUCT (ADMIN + MERCHANT)
@router.put("/update/")
async def update_product(
    product_id: int,
    product_data: ProductCreate,
    db: Session = Depends(get_db),
    user=Depends(role_required(["admin", "merchant"]))
):
    try:
        return ProductDetails(db, product_data).update_product(product_id)
    except Exception as e:
        raise e


# DELETE PRODUCT (ADMIN ONLY)
@router.delete("/delete/")
async def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    user=Depends(role_required(["admin"]))
):
    try:
        return ProductDetails(db, None).delete_product(product_id)
    except Exception as e:
        raise e

# POPULAR PRODUCTS
@router.get("/get_popular_products")
def get_popular_products(db: Session = Depends(get_db)):
    try:
        return ProductDetails(db, None).popular_products()
    except Exception as e:
        raise e


