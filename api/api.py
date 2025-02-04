# m fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal
from uuid import UUID

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Data Warehouse API"}

# # Create a new medical_data entry
# @app.post("/medical_datas/", response_model=schemas.MedicalData)
# def create_medical_data(medical_data: schemas.MedicalDataCreate, db: Session = Depends(get_db)):
#     return crud.create_medical_data(db=db, medical_data=medical_data)

# # Read all medical_data entries
# @app.get("/medical_datas/", response_model=list[schemas.MedicalData])
# def read_medical_datas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     return crud.get_medical_datas(db=db, skip=skip, limit=limit)

# Create a new detection_data entry
@app.post("/detection_datas/", response_model=schemas.DetectionData)
def create_detection_data(detection_data: schemas.DetectionDataCreate, db: Session = Depends(get_db)):
    return crud.create_detection_data(db=db, detection_data=detection_data)

# Read all detection_data entries
@app.get("/detection_datas/", response_model=list[schemas.DetectionData])
def read_detection_datas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_detection_datas(db=db, skip=skip, limit=limit)

# Update a medical_data entry
# @app.put("/medical_datas/{message_id}", response_model=schemas.MedicalData)
# def update_medical_data(message_id: UUID, medical_data: schemas.MedicalDataUpdate, db: Session = Depends(get_db)):
#     db_medical_data = crud.update_medical_data(db=db, message_id=message_id, medical_data=medical_data)
#     if db_medical_data is None:
#         raise HTTPException(status_code=404, detail="MedicalData not found")
#     return db_medical_data

# Delete a medical_data entry
# @app.delete("/medical_datas/{message_id}", response_model=schemas.MedicalData)
# def delete_medical_data(message_id: UUID, db: Session = Depends(get_db)):
#     db_medical_data = crud.delete_medical_data(db=db, message_id=message_id)
#     if db_medical_data is None:
#         raise HTTPException(status_code=404, detail="MedicalData not found")
#     return db_medical_data