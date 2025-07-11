# controllers/provider_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.dependencies import get_db
from services import provider_service  # 👈 Yeni ekledik

router = APIRouter(
prefix="/providers",
    tags=["🏥 Provider Operations"]
)

@router.post("/providers")
def create_provider(name: str, db: Session = Depends(get_db)):
    provider = provider_service.create_provider(db, name)
    return {"id": provider.id, "name": provider.name}

@router.get("/providers")
def list_providers(db: Session = Depends(get_db)):
    providers = provider_service.get_all_providers(db)
    return [{"id": p.id, "name": p.name} for p in providers]

@router.get("/providers/{provider_id}")
def get_provider(provider_id: int, db: Session = Depends(get_db)):
    provider = provider_service.get_provider_by_id(db, provider_id)
    return {"id": provider.id, "name": provider.name}

@router.put("/providers/{provider_id}")
def update_provider(provider_id: int, name: str, db: Session = Depends(get_db)):
    provider = provider_service.update_provider(db, provider_id, name)
    return {"message": "Sağlayıcı güncellendi", "provider": {"id": provider.id, "name": provider.name}}

@router.delete("/providers/{provider_id}")
def delete_provider(provider_id: int, db: Session = Depends(get_db)):
    return provider_service.delete_provider(db, provider_id)
