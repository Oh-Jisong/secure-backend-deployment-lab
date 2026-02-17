from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext

from app.core.config import JWT_SECRET, JWT_ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Demo users (for portfolio). Replace with DB later.
_demo_users = {
    "admin": pwd_context.hash("admin1234")
}

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int

@router.post("/login", response_model=TokenResponse)
def login(body: LoginRequest):
    hashed = _demo_users.get(body.username)
    if not hashed or not pwd_context.verify(body.password, hashed):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        subject=body.username,
        secret=JWT_SECRET,
        algorithm=JWT_ALGORITHM,
        expires_minutes=ACCESS_TOKEN_EXPIRE_MINUTES,
    )
    return {
        "access_token": token,
        "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    }
