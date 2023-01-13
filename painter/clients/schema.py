from pydantic import BaseModel


class Task(BaseModel):
    uid: int
    prompt: str
