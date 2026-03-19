from fastapi import FastAPI
from app.core.middleware import log_requests
from app.core.config import settings
from app.database.init_db import init_db
from app.users_module.routes import users_auth

app = FastAPI(title="Echo Chat Backend")

app.middleware("http")(log_requests)

@app.on_event("startup")
def on_startup():
    init_db()
    
app.include_router(users_auth.router)

@app.get("/")
def health_check():
    return {"message": "Echo backend is running"}