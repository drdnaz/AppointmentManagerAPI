import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base  # ✅ Uyarıyı çözdük

# ✅ Tam yol garantili
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "appointments.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_path}"

# ✅ Veritabanı bağlantısı
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Base tanımı (uyarı çözülmüş oldu)
Base = declarative_base()
