<<<<<<< HEAD
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
=======
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.models import Provider
from utils.dependencies import get_db


router = APIRouter()


# ➕ Yeni sağlayıcı oluştur (POST /providers)
@router.post("/providers")
def create_provider(name: str, db: Session = Depends(get_db)):
    provider = Provider(name=name)
    db.add(provider)
    db.commit()
    db.refresh(provider)
    return {"id": provider.id, "name": provider.name}

# 🔍 Tüm sağlayıcıları listele (GET /providers)
@router.get("/providers")
def list_providers(db: Session = Depends(get_db)):
    providers = db.query(Provider).all()
    return [{"id": p.id, "name": p.name} for p in providers]

# 🔍 Sağlayıcı detayını getir (GET /providers/{provider_id})
@router.get("/providers/{provider_id}")
def get_provider(provider_id: int, db: Session = Depends(get_db)):
    provider = db.query(Provider).filter(Provider.id == provider_id).first()
    if not provider:
        raise HTTPException(status_code=404, detail="Sağlayıcı bulunamadı")
    return {"id": provider.id, "name": provider.name}
>>>>>>> db66bb345e292369d0ea6432074d36fe2e74f74a
