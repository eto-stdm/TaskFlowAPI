from fastapi import FastAPI

from app.routers import tasks

app = FastAPI()

app.include_router(tasks.router)

@app.get("/")
def root():
    """Корневая директория"""
    return {"message": "Приложение по управлению задачами 'TaskFlow API' v1.1"}