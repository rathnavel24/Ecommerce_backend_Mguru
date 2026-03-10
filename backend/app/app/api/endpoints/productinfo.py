from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.app.Schemas.productinfo_schema import ProductCreate
from app.app.crud.productinfo_crud import ProductDetails
from app.app.api.deps import get_db
from app.app.api.deps import get_current_user

router = APIRouter(prefix="/products" ,tags=["Products"])

@router.get("/All-products")
async def get_products(db: Session = Depends(get_db)):
    try:
        return ProductDetails(db, None).get_all_products()
    except Exception as e:
        raise e

@router.post("/create-product")
async def create_product(product_data:ProductCreate, db: Session=Depends(get_db),
    user = Depends(get_current_user)):
    try:
        return ProductDetails(db,product_data).create_product()
    except Exception as e:
        raise e
    
@router.put("/update/")
async def update_product(product_id:int, product_data:ProductCreate,db: Session=Depends(get_db),
    user = Depends(get_current_user)):
    try:
        return ProductDetails(db,product_data).update_product(product_id)
    except Exception as e:
        raise e
    
@router.delete("/delete/")
async def delete_product(product_id:int,db:Session=Depends(get_db),
    user = Depends(get_current_user)):
    try: 
        return ProductDetails(db,None).delete_product(product_id)
    except Exception as e:
        raise e
        
