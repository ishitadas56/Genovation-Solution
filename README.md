 FastAPI Prompt App
A simple backend project for internship assignment.

✅ Features
User login with token (hardcoded)

Submit prompts and get dummy responses

View your prompt-response history

🚀 How to Run
Install dependencies:
pip install fastapi uvicorn

Run server:
uvicorn main:app --reload
Open browser
Visit: http://127.0.0.1:8000/docs


🔐 Login Users
json
Copy
Edit
{
  "alice": "password123",
  "bob": "secret"
}
Example curl
bash
Copy
Edit
curl -X POST http://127.0.0.1:8000/login/ -H "Content-Type: application/json" -d '{"username":"alice","password":"password123"}'

View Prompt History

bash
Copy
Edit
curl -X GET http://127.0.0.1:8000/history/ \
-H "Authorization: Bearer <your_token>"

Project Structure
main.py – App entrypoint

routes/ – All endpoints

auth.py – Token handling

models.py – Data models

README.md – This file
 Login system with hardcoded users

 Submit text prompts and receive fake AI-style responses

View user-specific prompt history with timestamps

 Token-based authentication (stored in memory)

