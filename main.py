from fastapi import FastAPI
from src.utils.db import Base,engine
from src.task.router import task_routes
from src.user.router import user_routes

Base.metadata.create_all(engine) #connection the database

app=FastAPI(title="My Task Management Application")
app.include_router(task_routes)
app.include_router(user_routes)