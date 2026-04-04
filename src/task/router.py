from fastapi import APIRouter, Depends, status
from src.task import controller
from src.task.dtos import TaskSchema,TaskResponseSchema
from src.utils.db import get_db
from typing import List
from sqlalchemy.orm import Session

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchema, db:Session=Depends(get_db)):
    return controller.create_task(body,db)

@task_routes.get("/get_task",response_model=List[TaskResponseSchema],status_code=status.HTTP_201_CREATED)
def get_task(db:Session=Depends(get_db)):
    return controller.get_task(db)

@task_routes.get("/get_task/{id}",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
def get_one_task(id:int,db:Session = Depends(get_db)):
    return controller.get_one_task(id,db)

@task_routes.put("/edit_task/{id}",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
def edit_task(body:TaskSchema,id:int,db:Session=Depends(get_db)):
    return controller.edit_task(body,id,db)

@task_routes.delete("/delete_task/{id}",response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id:int,db:Session=Depends(get_db)):
    return controller.delete_task(id,db)