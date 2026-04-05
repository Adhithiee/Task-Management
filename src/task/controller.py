from src.task.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.task.models import TaskModel
from fastapi import HTTPException

def create_task(body:TaskSchema,db:Session):
    new_task=TaskModel(
        title=body.title,
        desc=body.desc,
        is_completed=body.is_completed)
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

def get_task(db:Session):
    task=db.query(TaskModel).all()
    return task

def get_one_task(id:int,db:Session):
    task=db.query(TaskModel).get(id)

    if not task:
        raise HTTPException(404,detail="ID not found")
    return task

def edit_task(body:TaskSchema,id:int,db:Session):
    task=db.query(TaskModel).get(id)
    if not task:
        raise HTTPException(404,detail="ID not found")
    
    data = body.model_dump()
    for field,value in data.items():
        setattr(task,field,value)

    db.add(task)
    db.commit()
    db.refresh(task)

    return task

def delete_task(id:int,db:Session):
    task=db.query(TaskModel).get(id)
    if not task:
        raise HTTPException(404,details="ID not found")
    
    db.delete(task)
    db.commit()

    return None
    