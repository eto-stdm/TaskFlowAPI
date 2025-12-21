from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    text: str
    is_done: bool = False


tasks = []
test_data = [
{
  "text": "Создание приложения на FastAPI",
  "is_done": True
},
{
  "text": "Изучение OpenAPI",
  "is_done": False
},
{
  "text": "Создание аккаунта на GitHub",
  "is_done": True
},
{
  "text": "Изучение декораторов",
  "is_done": False
},
{
  "text": "Изучение Docker",
  "is_done": False
}
]
tasks += test_data


@app.get("/")
def root():
    return {"message": "Приложение по управлению задачами 'TaskFlow API' v1.0"}


@app.post("/tasks", response_model=list[Task])
def create_task(task: Task):
    tasks.append(task)
    return tasks


@app.get("/tasks", response_model=list[Task])
def list_task(limit: int = 100):
    return tasks[0:limit]


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    if task_id < len(tasks):
        return tasks.__getitem__(task_id) # tasks[task_id] == tasks.__getitem__(task_id) (не выдаёт предупреждение)
    else:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


@app.delete("/tasks/{task_id}", response_model=list[Task])
def delete_task(task_id: int) -> Task:
    if task_id < len(tasks):
        tasks.pop(task_id)
        return tasks
    else:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.put("/tasks/{task_id}", response_model=Task)
def change_state_of_task(task_id: int) -> Task:
    if task_id < len(tasks):
        tasks.__getitem__(task_id)["is_done"] = not tasks.__getitem__(task_id)["is_done"]
        return tasks.__getitem__(task_id)
    else:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")