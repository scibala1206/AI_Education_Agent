# repositories/user_repository.py
from models.user import User


class UserRepository:
    def __init__(self):
        self.users = []  # Simulates a database

    def create(self, user: User) -> User:
        user.id = len(self.users) + 1
        self.users.append(user)
        return user

    def get_all(self) -> list[User]:
        return self.users

    def get_by_id(self, user_id: int) -> User | None:
        return next((user for user in self.users if user.id == user_id), None)

    def update(self, user_id: int, updated_user: User) -> User | None:
        user = self.get_by_id(user_id)
        if user:
            user.name = updated_user.name
            user.email = updated_user.email
            return user
        return None

    def delete(self, user_id: int) -> bool:
        user = self.get_by_id(user_id)
        if user:
            self.users.remove(user)
            return True
        return False
