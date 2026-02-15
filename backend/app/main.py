from fastapi import FastAPI

app = FastAPI(title="Secure Backend Deployment Lab", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Secure Backend Deployment Lab Running"}