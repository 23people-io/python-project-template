from fastapi import APIRouter

from models.user_model import User
from services import users_service

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}")
async def get_user(user_id: int) -> User:
    return users_service.get_user(user_id)


@router.post("/")
async def create_user(user: User) -> User:
    return users_service.create_user(user)
