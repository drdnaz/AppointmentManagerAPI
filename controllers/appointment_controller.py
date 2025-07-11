from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.dependencies import get_db
from services import appointment_service
from datetime import datetime

router = APIRouter(
    prefix="/appointments",
    tags=["📅 Appointment Operations"]
)

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
# Randevu güncelle (PUT)
@router.put("/appointments/{appointment_id}")
def update_appointment(
    appointment_id: int,
    new_provider_id: int,
    new_datetime: datetime,
    db: Session = Depends(get_db)
):
    return appointment_service.update_appointment(db, appointment_id, new_provider_id, new_datetime)
# Sağlayıcıya ait randevuları getir

# Randevuyu iptal et (status = cancelled yap)
@router.put("/appointments/{appointment_id}/cancel")
def cancel_appointment(appointment_id: int, db: Session = Depends(get_db)):
    return appointment_service.cancel_appointment(db, appointment_id)
# 👤 Kullanıcının tüm randevularını getir
@router.get("/users/{user_id}/appointments")
def get_user_appointments(user_id: int, db: Session = Depends(get_db)):
    return appointment_service.get_appointments_by_user(db, user_id)

# 🏥 Sağlayıcının tüm randevularını getir
@router.get("/providers/{provider_id}/appointments")
def get_provider_appointments(provider_id: int, db: Session = Depends(get_db)):
    return appointment_service.get_appointments_by_provider(db, provider_id)
