from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError

from app.core.config import JWT_SECRET, JWT_ALGORITHM

bearer_scheme = HTTPBearer(auto_error=False)

def get_current_user(creds: HTTPAuthorizationCredentials = Depends(bearer_scheme)) -> dict:
    if creds is None or creds.scheme.lower() != "bearer":
        raise HTTPException(status_code=401, detail="Missing bearer token")

    token = creds.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    if payload.get("type") != "access":
        raise HTTPException(status_code=401, detail="Invalid token type")

    username = payload.get("sub")
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    return {"username": username}
