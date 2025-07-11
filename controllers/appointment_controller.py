from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.dependencies import get_db
from services import appointment_service
from datetime import datetime

router = APIRouter()

# ➕ Yeni randevu oluştur
@router.post("/appointments")
def create_appointment(user_id: int, provider_id: int, datetime_value: datetime, db: Session = Depends(get_db)):
    return appointment_service.create_appointment(db, user_id, provider_id, datetime_value)

# 🔍 Tüm randevuları listele
@router.get("/appointments")
def list_appointments(db: Session = Depends(get_db)):
    return appointment_service.get_all_appointments(db)

# Randevu sil (iptal et)
@router.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    return appointment_service.delete_appointment(db, appointment_id)
