from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.app.models.ecommerce_inventory import EcommerceInventory


class InventoryDetails:

    def __init__(self,db: Session, inventory_data):
        self.db = db
        self.inventory_data = inventory_data

    def get_all_products_inven(self):
        products = self.db.query(EcommerceInventory).filter(EcommerceInventory.status != "deleted").all()

        if not products:
            raise HTTPException(status_code=404, detail= "No product found")
        return products
        

    def create_inventory(self):
        if self.inventory_data.reserved_quantity > self.inventory_data.stock_quantity:
            raise HTTPException(status_code=400,detail="Reserved quantity cannot be greater than stock quantity")

        new_inventory = EcommerceInventory(
            product_id = self.inventory_data.product_id,
            stock_quantity = self.inventory_data.stock_quantity,
            reserved_quantity = self.inventory_data.reserved_quantity,
            status = self.inventory_data.status,
            created_by = self.inventory_data.created_by
        )
        self.db.add(new_inventory)
        self.db.commit()
        self.db.refresh(new_inventory)
        return{
            "msg" : "Inventory Created Successfully"
        }
    

    def update_inventory(self,inventoryy_id:int):
        if self.inventory_data.reserved_quantity > self.inventory_data.stock_quantity:
            raise HTTPException(status_code=400,detail="Reserved quantity cannot be greater than stock quantity")
        
        product = self.db.query(EcommerceInventory).filter(EcommerceInventory.inventory_id == inventoryy_id).first()

        if not product:
            raise HTTPException(status_code=404, detail= "Product not found")
        
        product.stock_quantity = self.inventory_data.stock_quantity
        product.reserved_quantity = self.inventory_data.reserved_quantity
        product.status = self.inventory_data.status

        self.db.commit()
        self.db.refresh(product)
        return{
            "msg" : "Product Updated Successfully"
        }
    

    def delete_inventory(self,inventoryyy_id = int):

        product = self.db.query(EcommerceInventory).filter(EcommerceInventory.inventory_id == inventoryyy_id).first()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        
        product.status = "deleted"
        self.db.commit()
        self.db.refresh(product)

        return {"message" : "Product Deleted Successfully"}
        




