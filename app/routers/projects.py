from fastapi import APIRouter, HTTPException # импорт классов для структуризации ручек и http-исключений

from app.test_data.projects import projects # импорт тестовых данных
from app.schemas.project import Project # импорт схемы

router = APIRouter(
    prefix="/projects", # автопрефикс к ручкам
    tags=["projects"] # группировка ручек в OpenAPI
)

@router.post("/", response_model=Project)
def create_project(project: Project):
    """Создание нового проекта"""
    projects.append(project)
    return project


@router.get("/", response_model=list[Project])
def list_project(limit: int = 20):
    """Вывод первых двадцати (по умолчанию) проектов"""
    return projects[0:limit]