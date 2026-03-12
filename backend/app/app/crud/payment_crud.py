from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.app.models.ecommerce_payments import EcommercePayments
import uuid

class PaymentsDetails:

    def __init__(self,db: Session,payment_data):
        self.db = db
        self.payment_data = payment_data


    def get_all_payments(self):
        payments = self.db.query(EcommercePayments).all()

        if not payments:
            raise HTTPException(status_code=404, detail= "No payment found")
        return payments

    def create_payment(self):

        transection_id = str(uuid.uuid4())

        new_payment = EcommercePayments(
            order_id = self.payment_data.order_id, 
            user_id = self.payment_data.user_id,
            payment_gateway = self.payment_data.payment_gateway,
            amount = self.payment_data.amount,
            transaction_id= transection_id,
            payment_method = self.payment_data.payment_method,
            payment_status = self.payment_data.payment_status
        )
        self.db.add(new_payment)
        self.db.commit()
        self.db.refresh(new_payment)
        return{
            "msg" : "Payment Created Successfully",
            "transection_id" : transection_id
        }
    
    def update_payment(self,paymentt_id:int):

        payment = self.db.query(EcommercePayments).filter(EcommercePayments.payment_id == paymentt_id).first()

        if not payment:
            raise HTTPException(status_code=404, detail= "Payment not found")
        
        payment.payment_gateway = self.payment_data.payment_gateway
        payment.amount = self.payment_data.amount
        payment.payment_method = self.payment_data.payment_method
        payment.payment_status = self.payment_data.payment_status

        self.db.commit()
        self.db.refresh(payment)
        return{
            "msg" : "Payment Updated Successfully"
        }
        
    