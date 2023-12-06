from pydantic import BaseModel

# define Todo model
class Todo(BaseModel):
    title: str
    description: str