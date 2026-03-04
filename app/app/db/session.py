from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

conn = "mysql+pymysql://2UzLbM74cdpvQ6S.root:1OqTxHRkMOc0H6ie@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/ecommerce"

engine = create_engine(
    conn,
    connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem"
        }
    }
)

sessionLocal = sessionmaker(bind=engine)

def get_db():
    db = sessionLocal()
    try :
        yield db
    finally:
        db.close()