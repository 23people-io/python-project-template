import random

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])


class User(BaseModel):
    id: int | None = None
    name: str
    email: str


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    return User(id=user_id, name="John Doe", email="john.doe@example.com")


@router.post("/", response_model=User)
async def create_user(user: User):
    user.id = random.randint(10, 1000)  # Simulate user creation and assign an ID  # noqa: S311
    return user
