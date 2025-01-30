# models/user.py
from pydantic import BaseModel
from typing import Optional

# User schema for request & response validation
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str  # Required during registration

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True  # Allows compatibility with ORMs
