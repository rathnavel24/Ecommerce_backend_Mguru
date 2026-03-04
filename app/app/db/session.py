from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

conn = "mysql+pymysql://root:1234@localhost/ecommerce"

engine = create_engine(conn)

sessionLocal = sessionmaker(bind=engine)
