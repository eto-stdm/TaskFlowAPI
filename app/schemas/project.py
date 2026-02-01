from pydantic import BaseModel, field_validator # импорт базовой модели pydantic и валидатора полей
# from app.schemas.user import User # импорт юзера для связи моделей (не используется)

class Project(BaseModel):
    name: str
    description: str = None
    participants: list[str]

    @field_validator("name")
    def validate_name(cls, value):
        if len(value) > 50:
            raise ValueError(f"name должен быть меньше 50 символов. Текущее значение: {value}")
        return value

    @field_validator("description")
    def validate_description(cls, value):
        if len(value) > 200:
            raise ValueError(f"description должен быть меньше 200 символов. Текущее значение: {value}")
        return value

    @field_validator("participants")
    def validate_participants(cls, value):
        if len(value) == 0:
            raise ValueError("participants должен содержать хотя бы одного участника")
        return value