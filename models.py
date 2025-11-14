from sqlalchemy import Column,Integer,String
from database import Base



class mySchoolClasses(Base):
    __tablename__ = "mySchoolClasses"
    id: int = Column(Integer, primary_key=True, index= True) # type: ignore    
    name: str = Column(String) # type: ignore
    schoolName: str = Column(String) # # type: ignore    
    teacherName: str = Column(String) # type: ignore
    studentCount : int = Column(Integer) # type: ignore