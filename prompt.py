from fastapi import APIRouter, Header, HTTPException
from models import PromptRequest, PromptResponse
from auth import get_username_from_token
from storage import user_history
from datetime import datetime
import random

responses = [
    "Interesting... Let's explore that idea.",
    "Let me think...",
    "Hmm, that's a good one!",
    "You got me thinking!"
]

router = APIRouter()

@router.post("/prompt/", response_model=PromptResponse)
def submit_prompt(data: PromptRequest, authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing token")

    token = authorization.split()[1]
    username = get_username_from_token(token)

    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")

    response = random.choice(responses)
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": data.prompt,
        "response": response
    }
    user_history[username].append(entry)
    return {"response": response}