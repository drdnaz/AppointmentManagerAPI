from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    appointments = relationship("Appointment", back_populates="user")

class Provider(Base):
    __tablename__ = "providers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    appointments = relationship("Appointment", back_populates="provider")

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    provider_id = Column(Integer, ForeignKey("providers.id"))
    datetime = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="active")
    user = relationship("User", back_populates="appointments")
    provider = relationship("Provider", back_populates="appointments")
