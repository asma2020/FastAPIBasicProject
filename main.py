from fastapi import FastAPI, Depends
import uvicorn
from pydantic import BaseModel, Field
from uuid import UUID
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind= engine)
def db_get():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class mySchoolClasses(BaseModel):    
    name: str = Field(min_length=1, max_length=100)
    schoolName: str = Field(min_length=1, max_length=100)
    teacherName: str = Field(min_length=1, max_length=100)
    studentCount: int = Field(gt=1, lt=100)


@app.get("/")
def resd_school_classes( db: Session = Depends(db_get)):
    return db.query(models.mySchoolClasses).all()

@app.post("/")
def create_school_class(MyschoolClasses : mySchoolClasses, db : Session = Depends(db_get)):
    school_classes = models.mySchoolClasses()
    school_classes.name = MyschoolClasses.name
    school_classes.schoolName = MyschoolClasses.schoolName
    school_classes.teacherName = MyschoolClasses.teacherName
    school_classes.studentCount = MyschoolClasses.studentCount
    db.add(school_classes)
    db.commit()
@app.put("/{school_class_id}")
def Update_School_Class(mySchoolclassId:int, MyschoolClass:mySchoolClasses,db: Session= Depends(db_get)):
    myschool_class = db.query(models.mySchoolClasses).filter(models.mySchoolClasses.id == mySchoolclassId).first()
    if myschool_class is None:
        print("There is noy any ID")
    myschool_class.name = MyschoolClass.name    
    myschool_class.name = MyschoolClass.name
    myschool_class.schoolName = MyschoolClass.schoolName
    myschool_class.teacherName = MyschoolClass.teacherName
    myschool_class.studentCount = MyschoolClass.studentCount
    db.add(myschool_class)
    db.commit()
    return  MyschoolClass

@app.delete("/{mySchoolclassId}")
def DeleteFromSchool(mySchoolclassId:int,db:Session = Depends(db_get)):
    my_class= db.query(models.mySchoolClasses).filter(models.mySchoolClasses.id==mySchoolclassId).first()

    if my_class is not None:
        db.query(models.mySchoolClasses).filter(models.mySchoolClasses.id==mySchoolclassId).delete()
        db.commit()
    
        




if __name__ =="__main__":
    uvicorn.run(app)
