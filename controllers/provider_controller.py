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
