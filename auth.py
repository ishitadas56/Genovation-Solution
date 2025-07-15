import uuid

users = {
    "alice": "password123",
    "bob": "secret"
}

tokens = {}

def authenticate_user(username: str, password: str):
    return users.get(username) == password

def generate_token(username: str):
    token = str(uuid.uuid4())
    tokens[token] = username
    return token

def get_username_from_token(token: str):
    return tokens.get(token)