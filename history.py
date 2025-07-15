from fastapi import APIRouter, Header, HTTPException
from models import PromptHistoryItem
from auth import get_username_from_token
from storage import user_history
from typing import List

router = APIRouter()

@router.get("/history/", response_model=List[PromptHistoryItem])
def get_history(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing token")

    token = authorization.split()[1]
    username = get_username_from_token(token)

    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")

    return user_history[username]