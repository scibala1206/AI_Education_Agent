# services/user_service.py
from sqlalchemy.orm import Session
from app.models.schema import User
from app.models.user import UserCreate, UserRead

    class UserRepository:
        @staticmethod
        def create_user(db: Session, user: UserCreate):
            """Create a new user in the database."""
            db_user = User(name=user.name, email=user.email, password=user.password)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user

        @staticmethod
        def get_user_by_id(db: Session, user_id: int):
            """Retrieve a user by ID."""
            return db.query(User).filter(User.id == user_id).first()

        @staticmethod
        def get_user_by_email(db: Session, email: str):
            """Retrieve a user by email."""
            return db.query(User).filter(User.email == email).first()

        @staticmethod
        def get_all_users(db: Session):
            """Retrieve all users."""
            return db.query(User).all()





