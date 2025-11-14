from .engine_sync import Base
from sqlalchemy.orm import Mapped, mapped_column

UsernameType = str

class User(Base):    
    __tablename__= "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str| None]= mapped_column(unique=True, default= None, nullable=True)
    password: Mapped[str]= mapped_column()