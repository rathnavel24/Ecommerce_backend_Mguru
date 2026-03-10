from app.app.models.ecommerce_user import Users
from app.app.core.security import verify_password, hash_password


class ChangePasswordCRUD:

    def __init__(self, db, user_id, old_password, new_password):
        self.db = db
        self.user_id = user_id
        self.old_password = old_password
        self.new_password = new_password

    def change(self):

        user = self.db.query(Users).filter(
            Users.user_id == self.user_id
        ).first()

        if not user:
            raise Exception("User not found")

        if not verify_password(self.old_password, user.password):
            raise Exception("Old password is incorrect")

        user.password = hash_password(self.new_password)

        self.db.commit()

        return {
            "message": "Password changed successfully"
        }