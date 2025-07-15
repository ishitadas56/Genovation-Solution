from fastapi import FastAPI
from routes import login, prompt, history

app = FastAPI()

app.include_router(login.router)
app.include_router(prompt.router)
app.include_router(history.router)