from pydantic import BaseModel, field_validator # импорт базовой модели pydantic и валидатора полей

class Task(BaseModel):
    text: str
    is_done: bool = False

    @field_validator("text") 
    def validate_text(cls, value): # cls - то же самое, что и self, только для декораторов
        if len(value) > 100:
            raise ValueError(f"text должен быть меньше 100 символов. Текущее значение: {value}")
        return value