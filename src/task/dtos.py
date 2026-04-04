from pydantic import BaseModel

class TaskSchema(BaseModel):
    title : str 
    desc : str
    is_completed : bool = False