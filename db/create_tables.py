# db/create_tables.py

from db.database import Base, engine
from models.models import User, Provider, Appointment  # bu satır çok önemli!

print("📢 Tablolar oluşturuluyor...")

Base.metadata.create_all(bind=engine)

print("✅ Tablolar başarıyla oluşturuldu.")
