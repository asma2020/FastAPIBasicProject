from sqlalchemy.ext.asyncio import async_sessionmaker,create_async_engine
from sqlalchemy.orm import DeclarativeBase,MappedAsDataclass

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./asyncdatabase.db"
engine = create_async_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})
SeasionLocal = async_sessionmaker(bind=engine, autoconnect= False,autoflush= False)

class Base(DeclarativeBase, MappedAsDataclass):
    pass



def get_db():
    db = SeasionLocal()
    try:
        yield db
    finally:
        db.close()