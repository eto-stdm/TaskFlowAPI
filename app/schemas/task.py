from typing import List # импорт класса "список"

from pydantic import BaseModel, field_validator # импорт базовой модели pydantic и валидатора полей
from pydantic_filters import BaseFilter, SearchField

# from fastapi_filter.contrib.sqlalchemy import Filter # импорт фильтров (нерабочий)
# from fastapi_filter import FilterDepends

class Task(BaseModel):
    text: str
    is_done: bool = False

    @field_validator("text") 
    def validate_text(cls, value): # cls - то же самое, что и self, только для декораторов
        if len(value) > 100:
            raise ValueError(f"text должен быть меньше 100 символов. Текущее значение: {value}")
        return value

class TaskFilter(BaseFilter): # класс для фильтрации (сейчас не используется)
    text: List[str] = None
    text__n: List[str] = None
    is_done: bool = None
    q: str = SearchField(target=["text"]) # поиск в поле "text"