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


def update_appointment(db: Session, appointment_id: int, new_provider_id: int, new_datetime: datetime):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Randevu bulunamadı")

    # Eğer çakışma varsa ve mevcut randevudan farklıysa hata ver
    if (
            db.query(Appointment).filter(
                Appointment.provider_id == new_provider_id,
                Appointment.datetime == new_datetime,
                Appointment.status == "active",
                Appointment.id != appointment_id  # kendi randevusu hariç!
            ).first()
    ):
        raise HTTPException(status_code=400, detail="Yeni tarih/saat başka bir randevu ile çakışıyor.")

    appointment.provider_id = new_provider_id
    appointment.datetime = new_datetime
    db.commit()
    db.refresh(appointment)
    return {
        "message": "Randevu güncellendi",
        "appointment": {
            "id": appointment.id,
            "user_id": appointment.user_id,
            "provider_id": appointment.provider_id,
            "datetime": appointment.datetime,
            "status": appointment.status
        }
    }


def get_appointments_by_provider(db: Session, provider_id: int):
    return db.query(Appointment).filter(Appointment.provider_id == provider_id).all()


def cancel_appointment(db: Session, appointment_id: int):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Randevu bulunamadı")
    appointment.status = "cancelled"
    db.commit()
    db.refresh(appointment)
    return {"message": "Randevu iptal edildi"}


def get_appointments_by_user(db: Session, user_id: int):
    return db.query(Appointment).filter(Appointment.user_id == user_id).all()
