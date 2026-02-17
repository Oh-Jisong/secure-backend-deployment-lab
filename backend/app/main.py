from fastapi import FastAPI

from app.auth.router import router as auth_router
from app.api.router import router as api_router

app = FastAPI(title="Secure Backend Deployment Lab", version="0.1.0")

app.include_router(auth_router)
app.include_router(api_router)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Secure Backend Deployment Lab Running"}

from fastapi import FastAPI
