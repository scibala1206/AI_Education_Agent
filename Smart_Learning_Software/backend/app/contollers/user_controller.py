from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.user_service import UserService
from app.models.user import UserCreate, UserRead
from config.db import database
from app.repositories.user_repository import UserRepository

router = APIRouter(prefix="/users", tags=["Users"])

# Dependency to get the database session
def get_db():
    with database as db:
        yield db

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user."""
    existing_user = UserRepository.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return UserService.create_user(db, user)

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Retrieve a user by ID."""
    user = UserService.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=list[UserRead])
def get_all_users(db: Session = Depends(get_db)):
    """Retrieve all users."""
    return UserService.get_all_users(db)
