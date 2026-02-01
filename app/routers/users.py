from fastapi import APIRouter, HTTPException # импорт классов для структуризации ручек и http-исключений

from app.test_data.users import users # импорт тестовых данных
from app.schemas.user import User # импорт схемы

router = APIRouter(
    prefix="/users", # автопрефикс к ручкам
    tags=["users"] # группировка ручек в OpenAPI
)

@router.post("/", response_model=User)
def create_user(user: User):
    """Создание нового пользователя"""
    users.append(user)
    return user


@router.get("/", response_model=list[User])
def list_user(limit: int = 10):
    """Вывод первых десяти (по умолчанию) пользователей"""
    return users[0:limit]