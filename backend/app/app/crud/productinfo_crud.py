from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.app.models.ecommerce_productinfo import EcommerceProductInfo

class ProductDetails:

    def __init__(self, db: Session,product_data):
        self.db = db
        self.product_data = product_data

    def get_all_products(self):
        products = self.db.query(EcommerceProductInfo).filter(EcommerceProductInfo.status != "deleted").all()

        if not products:
            raise HTTPException(status_code=404, detail="No products found")
        return products


    def create_product(self):

        new_product = EcommerceProductInfo(
            product_name = self.product_data.product_name,
            categorie_id = self.product_data.category_id,
            price = self.product_data.product_price,
            discount_percent = self.product_data.discount_per,
            description = self.product_data.product_description,
            image_url = self.product_data.image_url

        )
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return{
            "msg" : "Product Created Successfully"
        }
    
    def update_product(self,productt_id:int):

        product = self.db.query(EcommerceProductInfo).filter(EcommerceProductInfo.product_id == productt_id).first()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        
        product.product_name = self.product_data.product_name
        product.categorie_id = self.product_data.category_id
        product.price = self.product_data.product_price
        product.discount_percent = self.product_data.discount_per
        product.description = self.product_data.product_description
        product.image_url = self.product_data.image_url
        product.status = self.product_data.status

        self.db.commit()
        self.db.refresh(product)
        return{
            "msg" : "Product Updated Successfully"
        }
    
    def delete_product(self,producttt_id = int):
        product = self.db.query(EcommerceProductInfo).filter(EcommerceProductInfo.product_id == producttt_id).first()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found") 
        
        product.status = "deleted"
        self.db.commit()
        self.db.refresh(product)

        return{"message" : " Product Deleted Successfully"}
        






