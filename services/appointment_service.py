# services/appointment_service.py

from sqlalchemy.orm import Session
from models.models import Appointment
from datetime import datetime
from fastapi import HTTPException

def is_conflict(db: Session, provider_id: int, datetime_value: datetime) -> bool:
    return db.query(Appointment).filter(
        Appointment.provider_id == provider_id,
        Appointment.datetime == datetime_value,
        Appointment.status == "active"
    ).first() is not None

def create_appointment(db: Session, user_id: int, provider_id: int, datetime_value: datetime):
    if is_conflict(db, provider_id, datetime_value):
        raise HTTPException(status_code=400, detail="Bu sağlayıcı için bu saatte zaten bir randevu var.")

    new_appointment = Appointment(
        user_id=user_id,
        provider_id=provider_id,
        datetime=datetime_value,
        status="active"
    )
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return new_appointment

def get_all_appointments(db: Session):
    return db.query(Appointment).all()

def delete_appointment(db: Session, appointment_id: int):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Randevu bulunamadı")
    db.delete(appointment)
    db.commit()
    return {"message": "Randevu silindi"}
