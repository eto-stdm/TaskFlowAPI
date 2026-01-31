from fastapi import APIRouter, HTTPException

from app.test_data.tasks import tasks
from app.schemas.task import Task

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@router.post("/", response_model=list[Task])
def create_task(task: Task):
    """Создание новой задачи"""
    tasks.append(task)
    return tasks


@router.get("/", response_model=list[Task])
def list_task(limit: int = 100):
    """Вывод первых ста (по умолчанию) задач"""
    return tasks[0:limit] # я не знаю, как пофиксить это предупреждение


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    """Вывод определённой задачи по индексу"""
    if task_id < len(tasks):
        return tasks.__getitem__(task_id)
        # return tasks[task_id] # выдаёт предупреждение
    else:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


@router.delete("/{task_id}", response_model=list[Task])
def delete_task(task_id: int) -> Task:
    """Удаление задачи по индексу"""
    if task_id < len(tasks):
        tasks.pop(task_id)
        return tasks
    else:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@router.put("/{task_id}", response_model=Task)
def change_state_of_task(task_id: int) -> Task:
    """Изменение состояния задачи (завершено / не завершено)"""
    if task_id < len(tasks):
        tasks.__getitem__(task_id)["is_done"] = not tasks.__getitem__(task_id)["is_done"]
        return tasks.__getitem__(task_id)
    else:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")