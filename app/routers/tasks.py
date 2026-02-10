from typing import TypeVar # импорт класса для создания обобщённого типа

from fastapi import APIRouter, HTTPException, Query # импорт классов для структуризации ручек, создания http-исключений и запросов
from fastapi_pagination import Page, paginate # импорт класса "страница" и функции пагинации
from fastapi_pagination.customization import CustomizedPage, UseParamsFields # импорт кастомизации параметров для ↑

from app.test_data.tasks import tasks # импорт тестовых данных
from app.schemas.task import Task # импорт схемы

router = APIRouter( # экземпляр роутера
    prefix="/tasks", # автопрефикс к ручкам
    tags=["tasks"] # группировка ручек в OpenAPI
)

T = TypeVar("T") # обобщённый тип

CustomPage = CustomizedPage[ # создаём кастомный вывод по страницам (пагинация)
    Page[T],
    UseParamsFields( # параметры: по умолчанию, ge=минимум, le=максимум, название
        size=Query(20, ge=1, le=100, alias="pageSize"), # size - размер страницы
        page=Query(1, ge=1, alias="pageNumber"), # page - номер страницы
    ),
]


@router.post("/", response_model=Task)
def create_task(task: Task):
    """Создание новой задачи"""
    tasks.append(task)
    return task


@router.get("/", response_model=CustomPage[Task]) # CustomPage для пагинации
def list_task(text_: str = None, is_done_: bool = None): # атрибуты для фильтрации
    """Вывод первых двадцати (по умолчанию) задач"""
    filtered = list() # для отфильтрованных объектов

    if text_ and is_done_ != None: # оба фильтра
        for t in tasks:
            if text_.lower() in t["text"].lower() and is_done_ is t["is_done"]:
                filtered.append(t)
        return paginate(filtered)

    if text_:
        for t in tasks:
            if text_.lower() in t["text"].lower():
                filtered.append(t)
        return paginate(filtered)

    if is_done_ != None:
        for t in tasks:
            if is_done_ is t["is_done"]:
                filtered.append(t)
        return paginate(filtered)

    return paginate(tasks) # без фильтров


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    """Вывод определённой задачи по индексу"""
    if task_id < len(tasks):
        return tasks.__getitem__(task_id)
    else:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


@router.delete("/{task_id}", response_model=bool)
def delete_task(task_id: int) -> bool:
    """Удаление задачи по индексу"""
    if task_id < len(tasks):
        tasks.pop(task_id)
        return True
    else:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@router.put("/{task_id}", response_model=Task)
def change_state_of_task(task_id: int) -> Task:
    """Изменение состояния задачи (завершена / не завершена)"""
    if task_id < len(tasks):
        tasks.__getitem__(task_id)["is_done"] = not tasks.__getitem__(task_id)["is_done"]
        return tasks.__getitem__(task_id)
    else:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")