from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    username: str
    password: str
    name: str
    email: EmailStr

    @field_validator("username")
    def validate_username(cls, value):
        if len(value) < 3 or len(value) > 30:
            raise ValueError(f"username должен быть в промежутке от 3 до 30 символов. Текущее значение: {value}")
        return value

    @field_validator("password")
    def validate_password(cls, value):
        if len(value) < 10 or len(value) > 50:
            raise ValueError(f"password должен быть в промежутке от 10 до 50 символов. Текущее значение: {value}")
        return value

    @field_validator("name")
    def validate_name(cls, value):
        if len(value) > 30:
            raise ValueError(f"name должен быть меньше 30 символов. Текущее значение: {value}")
        return value