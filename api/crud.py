# crud.py
from sqlalchemy.orm import Session
from . import models, schemas

# CRUD operations for DetectionData
def get_detection_datas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.DetectionData).offset(skip).limit(limit).all()

def create_detection_data(db: Session, detection_data: schemas.DetectionDataCreate):
    db_detection_data = models.DetectionData(**detection_data.dict())
    db.add(db_detection_data)
    db.commit()
    db.refresh(db_detection_data)
    return db_detection_data

# CRUD operations for MedicalData
def get_medical_datas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.MedicalData).offset(skip).limit(limit).all()

def create_medical_data(db: Session, medical_data: schemas.MedicalDataCreate):
    db_medical_data = models.MedicalData(**medical_data.dict())
    db.add(db_medical_data)
    db.commit()
    db.refresh(db_medical_data)
    return db_medical_data

def update_medical_data(db: Session, message_id: str, medical_data: schemas.MedicalDataUpdate):
    db_medical_data = db.query(models.MedicalData).filter(models.MedicalData.message_id == message_id).first()
    if db_medical_data is None:
        return None
    for key, value in medical_data.dict().items():
        setattr(db_medical_data, key, value)
    db.commit()
    db.refresh(db_medical_data)
    return db_medical_data

def update_detection_data(db: Session, id: int, detection_data: schemas.DetectionDataUpdate):
    db_detection_data = db.query(models.DetectionData).filter(models.DetectionData.id == id).first()
    if db_detection_data is None:
        return None
    for key, value in detection_data.dict().items():
        setattr(db_detection_data, key, value)
    db.commit()
    db.refresh(db_detection_data)
    return db_detection_data

def delete_medical_data(db: Session, message_id: str):
    db_medical_data = db.query(models.MedicalData).filter(models.MedicalData.message_id == message_id).first()
    if db_medical_data is None:
        return None
    db.delete(db_medical_data)
    db.commit()
    return db_medical_data

def delete_detection_data(db: Session, id: int):
    db_detection_data = db.query(models.DetectionData).filter(models.DetectionData.id == id).first()
    if db_detection_data is None:
        return None
    db.delete(db_detection_data)
    db.commit()
    return db_detection_data