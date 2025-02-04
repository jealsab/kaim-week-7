# schemas.py
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from datetime import datetime

class DetectionDataBase(BaseModel):
    image_path: str
    box_coordinates: str
    confidence_score: float
    class_label: str

class DetectionDataCreate(DetectionDataBase):
    pass
class DetectionDataUpdate(DetectionDataBase):
    image_path: Optional[str] = None
    box_coordinates: Optional[str] = None
    confidence_score: Optional[float] = None
    class_label: Optional[str] = None

class DetectionData(DetectionDataBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode: True

class MedicalDataBase(BaseModel):
    sender_id: str
    message_text: str
    channel: str
class MedicalDataUpdate(MedicalDataBase):
    sender_id: Optional[str] = None
    message_text: Optional[str] = None
    channel: Optional[str] = None


class MedicalDataCreate(MedicalDataBase):
    pass

class MedicalData(MedicalDataBase):
    message_id: UUID

    class Config:
        orm_mode: True