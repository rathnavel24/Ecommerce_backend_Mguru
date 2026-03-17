from fastapi import APIRouter, Depends, File, Form, UploadFile, HTTPException
from sqlalchemy.orm import Session
from app.app.Schemas.productinfo_schema import ProductCreate
from app.app.crud.productinfo_crud import ProductDetails
from app.app.api.deps import get_db
from app.app.api.deps import get_current_user
from app.app.api.deps import role_required
from app.app.crud.image_services import upload_image

from fastapi import APIRouter
from sqlalchemy.orm import Session
from decimal import Decimal
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

@router.get("/products/{product_id}")
def get_products_by_category(product_id: int, db: Session = Depends(get_db)):
    return ProductDetails(db, None).get_product_by_productid(product_id)


# CREATE PRODUCT (ADMIN + MERCHANT)
@router.post("/create_product")
async def create_product(
    product_name: str = Form(...),
    category_id: int = Form(...),
    product_price: Decimal = Form(...),
    discount_per: Decimal | None = Form(None),
    product_description: str | None = Form(None),
    status: str = Form("active"),
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    user=Depends(role_required(["admin", "merchant"])),
    user_id=Depends(get_current_user)
):
    try:
       image_url = upload_image(image)
       product_dict = {
            "product_name" : product_name,
            "categorie_id" : category_id,
            "price" : product_price,
            "discount_percent" : discount_per,
            "description" : product_description,
            "image_url" : image_url,
            "createdby" : user_id,
            "status" : status  
       }
       return ProductDetails(db, product_dict).create_product(user_id.get("user_id"))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

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
    

@router.get("/search_products")
def prod_search(product_name:str,db:Session=Depends(get_db)):
    product = ProductDetails(db,None).search_products(product_name)    
    return product      


