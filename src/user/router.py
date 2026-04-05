from fastapi import APIRouter,Depends,status,Request
from typing import List
from src.user.dtos import UserSchema,UserReponseSchema,LoginSchema
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.user import controller

user_routes = APIRouter(prefix="/user")

@user_routes.post("/register",response_model=UserReponseSchema,status_code=status.HTTP_201_CREATED)
def register(body:UserSchema,db:Session=Depends(get_db)):
    return controller.register(body,db)

@user_routes.post("/login",status_code=status.HTTP_200_OK)
def login(body:LoginSchema,db:Session=Depends(get_db)):
    return controller.login(body,db)

@user_routes.get("/is_auth",response_model=UserReponseSchema ,status_code=status.HTTP_200_OK)
def is_auth(request:Request,db:Session=Depends(get_db)):
    return controller.is_auth(request,db)

@user_routes.get("/get_users",response_model=List[UserReponseSchema],status_code=status.HTTP_200_OK)
def get_all_users(db:Session=Depends(get_db)):
    return controller.get_all_user(db)

@user_routes.get("/get_user_by_id/{id}",response_model=UserReponseSchema,status_code=status.HTTP_200_OK)
def get_user_by_id(id:int,db:Session=Depends(get_db)):
    return controller.get_user_by_id(id,db)