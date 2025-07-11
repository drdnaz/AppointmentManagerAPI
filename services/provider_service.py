# services/provider_service.py

from sqlalchemy.orm import Session
from models.models import Provider
from fastapi import HTTPException

def create_provider(db: Session, name: str):
    provider = Provider(name=name)
    db.add(provider)
    db.commit()
    db.refresh(provider)
    return provider

def get_all_providers(db: Session):
    return db.query(Provider).all()

def get_provider_by_id(db: Session, provider_id: int):
    provider = db.query(Provider).filter(Provider.id == provider_id).first()
    if not provider:
        raise HTTPException(status_code=404, detail="Sağlayıcı bulunamadı")
    return provider

def update_provider(db: Session, provider_id: int, name: str):
    provider = db.query(Provider).filter(Provider.id == provider_id).first()
    if not provider:
        raise HTTPException(status_code=404, detail="Sağlayıcı bulunamadı")
    provider.name = name
    db.commit()
    db.refresh(provider)
    return provider

def delete_provider(db: Session, provider_id: int):
    provider = db.query(Provider).filter(Provider.id == provider_id).first()
    if not provider:
        raise HTTPException(status_code=404, detail="Sağlayıcı bulunamadı")
    db.delete(provider)
    db.commit()
    return {"message": "Sağlayıcı silindi"}
