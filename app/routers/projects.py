from fastapi import APIRouter, HTTPException

from app.test_data.projects import projects
from app.schemas.project import Project

router = APIRouter(
    prefix="/projects",
    tags=["projects"]
)

@router.post("/", response_model=list[Project])
def create_project(project: Project):
    """Создание нового проекта"""
    projects.append(project)
    return projects


@router.get("/", response_model=list[Project])
def list_project(limit: int = 20):
    """Вывод первых двадцати (по умолчанию) проектов"""
    return projects[0:limit]