# models.py
from sqlalchemy import Column, Integer, String, Float, Text, TIMESTAMP, UUID
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID as pUUID
import uuid
from .database import Base

class DetectionData(Base):
    __tablename__ = "detection_datas"

    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(Text, nullable=False)
    box_coordinates = Column(Text, nullable=False)
    confidence_score = Column(Float, nullable=False)
    class_label = Column(Text, nullable=False)
    timestamp = Column(TIMESTAMP, server_default=func.now())

class MedicalData(Base):
    __tablename__ = "medical_datas"

    message_id = Column(pUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sender_id = Column(String, nullable=False)
    message_text = Column(Text, nullable=False)
    channel = Column(Text, nullable=False)