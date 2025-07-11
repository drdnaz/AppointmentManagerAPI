# controllers/user_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.dependencies import get_db
from services import user_service

router = APIRouter( prefix="/users",
    tags=["👤  User Operations"]
)

@router.post("/users")
def create_user(name: str, db: Session = Depends(get_db)):
    user = user_service.create_user(db, name)
    return {"id": user.id, "name": user.name}

@router.get("/users")
def list_users(db: Session = Depends(get_db)):
    users = user_service.get_all_users(db)
    return [{"id": u.id, "name": u.name} for u in users]

@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db, user_id)
    return {"id": user.id, "name": user.name}

@router.put("/users/{user_id}")
def update_user(user_id: int, name: str, db: Session = Depends(get_db)):
    user = user_service.update_user(db, user_id, name)
    return {"message": "Kullanıcı güncellendi", "user": {"id": user.id, "name": user.name}}

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_service.delete_user(db, user_id)
    return {"message": "Kullanıcı silindi"}
