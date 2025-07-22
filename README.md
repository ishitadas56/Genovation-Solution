fastapi_prompt_app/
│
├── main.py # App startup and FastAPI instance
├── auth.py # User login and token storage
├── storage.py # In-memory storage for tokens and prompts
├── models.py # Pydantic request/response models
└── routes/
├── login.py # /login endpoint
├── prompt.py # /prompt endpoint
└── history.py # /history endpoint
step-1 Install Required Python Packages
step-2  Run the Application
step-3 Login and Get Token
step-4 Authorize Token in Swagger UI
step-5 Submit Prompt – POST /prompt/
step-6  View Prompt History – GET /history/
