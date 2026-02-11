import random

from models.user_model import User


def get_user(user_id: int) -> User:

    return User(id=user_id, name="John Doe", email="john.doe@example.com")


def create_user(user: User) -> User:

    user_id: int = random.randint(10, 1000)  # noqa: S311 # NOSONAR

    return User(id=user_id, name=user.name, email=user.email)
