from fastapi import APIRouter
from app.controllers.user_controller import router as user_router

# Create a new router instance for all user-related routes
router = APIRouter()

# Include the user routes
router.include_router(user_router)
