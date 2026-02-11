from fastapi import FastAPI # импорт класса приложения

from app.routers import tasks, users, projects # импорт ручек
from fastapi_pagination import add_pagination # импорт добавления пагинации

app = FastAPI() # создание приложения
add_pagination(app) # добавление пагинации

app.include_router(tasks.router) # подключение ручек
app.include_router(projects.router) # ↑
app.include_router(users.router) # ↑

from app.core.db import run
import asyncio

asyncio.run(run())

@app.get("/")
def root():
    """Корневая директория"""
    return {"message": "Приложение по управлению задачами 'TaskFlow API' v1.1"}