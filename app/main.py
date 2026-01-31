from fastapi import FastAPI

from app.routers import tasks, users, projects

app = FastAPI()

app.include_router(tasks.router)
app.include_router(projects.router)
app.include_router(users.router)

@app.get("/")
def root():
    """Корневая директория"""
    return {"message": "Приложение по управлению задачами 'TaskFlow API' v1.1"}