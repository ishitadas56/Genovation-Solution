from fastapi import APIRouter, HTTPException
from models import LoginRequest, LoginResponse
from auth import authenticate_user, generate_token

router = APIRouter()

@router.post("/login/", response_model=LoginResponse)
def login(data: LoginRequest):
    if not authenticate_user(data.username, data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = generate_token(data.username)
    return {"token": token}