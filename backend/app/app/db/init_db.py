from app.app.db.session import engine
from app.app.db.base import Base
import app.app.models

def init_db():
    Base.metadata.create_all(bind=engine)