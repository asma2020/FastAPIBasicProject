from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DABASE_URL = "sqlite:///./blogdb.db"
engine = create_engine(SQLALCHEMY_DABASE_URL, connect_args= {"check_same_thread":False})
SesionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base = declarative_base()
def get_db():
    db = SesionLocal()
    try:        
        yield db
    finally:
        db.close()
        