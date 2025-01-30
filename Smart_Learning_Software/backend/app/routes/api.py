# routes/api.py
from fastapi import FastAPI
from controllers.user_controller import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/api")
