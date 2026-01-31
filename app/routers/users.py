from fastapi import APIRouter, HTTPException

from app.test_data.users import users
from app.schemas.user import User

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=list[User])
def create_user(user: User):
    """Создание нового пользователя"""
    users.append(user)
    return users


@router.get("/", response_model=list[User])
def list_user(limit: int = 10):
    """Вывод первых десяти (по умолчанию) пользователей"""
    return users[0:limit]