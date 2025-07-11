# main.py (güncel hali)

from fastapi import FastAPI
from controllers.appointment_controller import router as appointment_router
from controllers.user_controller import router as user_router
from controllers.provider_controller import router as provider_router

app = FastAPI()

app.include_router(appointment_router)
app.include_router(user_router)
app.include_router(provider_router)

@app.get("/")
def read_root():
    return {"message": "AppointmentManagerAPI çalışıyor!"}
