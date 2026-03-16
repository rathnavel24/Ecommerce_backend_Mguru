from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.app.models.ecommerce_productinfo import EcommerceProductInfo
from app.app.models.ecommerce_categories import EcommerceCategories
from sqlalchemy import func


import random

class ProductDetails:

    def __init__(self, db: Session,product_data):
        self.db = db
        self.product_data = product_data

    def get_all_products(self):

        products = self.db.query(EcommerceProductInfo)\
            .filter(EcommerceProductInfo.status != "deleted")\
            .all()

        if not products:
            raise HTTPException(status_code=404, detail="No products found")

        result = []

        for product in products:

            product_data = {
                "price": product.price,
                "status": product.status,
                "discount_percent": product.discount_percent,
                "createdat": product.createdat,
                "description": product.description,
                "updatedat": product.updatedat,
                "image_url": product.image_url,
                "createdby": product.createdby,
                "sku": product.sku,
                "product_name": product.product_name,
                "rating": product.rating,
                "product_id": product.product_id,
                "total_reviews": product.total_reviews,
                "tag": product.tag,
                "category_name": product.category.name
            }

            result.append(product_data)
        random.seed(42)
        random.shuffle(result)

        return result


    def create_product(self,user_id):

        new_product = EcommerceProductInfo(
            product_name = self.product_data.get("product_name"),
            categorie_id = self.product_data.get("categorie_id"),
            price = self.product_data.get("price"),
            discount_percent = self.product_data.get("discount_percent"),
            description = self.product_data.get("description"),
            image_url = self.product_data.get("image_url"),
            createdby = user_id,
            status = self.product_data.get("status")  
        )
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return{
            "msg" : "Product Created Successfully"
        }
    
    def update_product(self, product_id: int):

        product = self.db.query(EcommerceProductInfo)\
            .filter(EcommerceProductInfo.product_id == product_id)\
            .first()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        update_data = self.product_data.dict(exclude_unset=True)

        field_map = {
            "product_price": "price",
            "category_id": "categorie_id",
            "product_description": "description",
            "discount_per": "discount_percent"
        }

        for key, value in update_data.items():
            db_field = field_map.get(key, key)
            setattr(product, db_field, value)

        self.db.commit()
        self.db.refresh(product)

        return {"msg": "Product Updated Successfully"}
    
    def delete_product(self,producttt_id = int):
        product = self.db.query(EcommerceProductInfo).filter(EcommerceProductInfo.product_id == producttt_id).first()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found") 
        
        product.status = "deleted"
        self.db.commit()
        self.db.refresh(product)

        return{"message" : " Product Deleted Successfully"}
    
    def popular_products(self):

        popularproducts = self.db.query(EcommerceProductInfo)\
            .filter(EcommerceProductInfo.status != "deleted")\
            .order_by(EcommerceProductInfo.rating.desc()).limit(4)

        if not popularproducts:
            raise HTTPException(status_code=404, detail="No products found")

        result = []

        for product in popularproducts:

            product_data = {
                "price": product.price,
                "status": product.status,
                "discount_percent": product.discount_percent,
                "createdat": product.createdat,
                "description": product.description,
                "updatedat": product.updatedat,
                "image_url": product.image_url,
                "createdby": product.createdby,
                "sku": product.sku,
                "product_name": product.product_name,
                "rating": product.rating,
                "product_id": product.product_id,
                "total_reviews": product.total_reviews,
                "tag": product.tag,
                "category_name": product.category.name
            }

            result.append(product_data)

        random.shuffle(result)

        return result
        

    def get_products_by_category(self, category_id: int):

        products = self.db.query(EcommerceProductInfo)\
            .filter(EcommerceProductInfo.categorie_id == category_id)\
            .filter(EcommerceProductInfo.status != "deleted")\
            .all()

        if not products:
            raise HTTPException(status_code=404, detail="No products found")

        result = []

        for product in products:

            product_data = {
                "price": product.price,
                "status": product.status,
                "discount_percent": product.discount_percent,
                "createdat": product.createdat,
                "description": product.description,
                "updatedat": product.updatedat,
                "image_url": product.image_url,
                "createdby": product.createdby,
                "sku": product.sku,
                "product_name": product.product_name,
                "rating": product.rating,
                "product_id": product.product_id,
                "total_reviews": product.total_reviews,
                "tag": product.tag,
                "category_name": product.category.name
            }

            result.append(product_data)


        return result
    def get_product_by_productid(self,id):
            product = self.db.query(EcommerceProductInfo)\
                .filter(EcommerceProductInfo.product_id == id)\
                .filter(EcommerceProductInfo.status != "deleted")\
                .first()
            if not product:
                raise HTTPException(status_code=404, detail="No products found")
            
            product = {
                    "price": product.price,
                    "status": product.status,
                    "discount_percent": product.discount_percent,
                    "createdat": product.createdat,
                    "description": product.description,
                    "updatedat": product.updatedat,
                    "image_url": product.image_url,
                    "createdby": product.createdby,
                    "sku": product.sku,
                    "product_name": product.product_name,
                    "rating": product.rating,
                    "product_id": product.product_id,
                    "total_reviews": product.total_reviews,
                    "tag": product.tag,
                    "category_name": product.category.name
                }
            
            return product

    def get_merchant_products(self, user_id):

        products = self.db.query(EcommerceProductInfo)\
            .filter(EcommerceProductInfo.createdby == user_id)\
            .filter(EcommerceProductInfo.status != "deleted")\
            .all()

        if not products:
            raise HTTPException(status_code=404, detail="No products found")

        result = []

        for product in products:
            product_data = {
                "price": product.price,
                "status": product.status,
                "discount_percent": product.discount_percent,
                "createdat": product.createdat,
                "description": product.description,
                "updatedat": product.updatedat,
                "image_url": product.image_url,
                "createdby": product.createdby,
                "sku": product.sku,
                "product_name": product.product_name,
                "rating": product.rating,
                "product_id": product.product_id,
                "total_reviews": product.total_reviews,
                "tag": product.tag,
                "category_name": product.category.name
            }

            result.append(product_data)

        return result
    

    def search_products(self, product_name: str):
        products = self.db.query(EcommerceProductInfo.product_id,EcommerceProductInfo.product_name)\
           .filter(EcommerceProductInfo.product_name.ilike(f"%{product_name}%"))\
           .filter(EcommerceProductInfo.status != "deleted")\
           .limit(10).all()
        if not products:
                raise HTTPException(status_code=404, detail="No products found")
        
        result = []

        for product in products:
            result.append({
                "product_id" : product.product_id,
                "product_name" : product.product_name
                
            })
        return result
       
    
       
