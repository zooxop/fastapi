from pydantic import BaseModel

class Item(BaseModel):
    item: str
    status: str
    
class Todo(BaseModel):
    id: int
    item: Item

class TodoItem(BaseModel):
    item: Item

    class Config:
        schema_extra = { 
            "example": { 
                "item": "Read the next chapter of the book."
            }
        }
        