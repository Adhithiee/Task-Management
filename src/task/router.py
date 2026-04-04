from fastapi import APIRouter, Depends
from src.task import controller
from src.task.dtos import TaskSchema
from src.utils.db import get_db

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create")
def create_task(body:TaskSchema, db=Depends(get_db)):
    return controller.create_task(body,db)

@task_routes.get("/get_task")
def get_task(db=Depends(get_db)):
    return controller.get_task(db)

@task_routes.get("/get_task/{id}")
def get_one_task(id:int,db = Depends(get_db)):
    return controller.get_one_task(id,db)