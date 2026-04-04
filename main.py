from fastapi import FastAPI
from src.utils.db import Base,engine
from src.task.models import TaskModel
from src.task.router import task_routes

Base.metadata.create_all(engine) #connection the database

app=FastAPI(title="My Task Management Application")
app.include_router(task_routes)