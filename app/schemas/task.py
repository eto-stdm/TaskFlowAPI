from pydantic import BaseModel

class Task(BaseModel):
    text: str
    is_done: bool = False

