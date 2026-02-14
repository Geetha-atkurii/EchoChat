from fastapi import FastAPI
from app.core.middleware import log_requests
from app.core.config import settings
from app.database.init_db import init_db

app = FastAPI(title="Echo Chat Backend")

app.middleware("http")(log_requests)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def health_check():
    return {"message": "Echo backend is running"}

print(settings.DB_NAME)