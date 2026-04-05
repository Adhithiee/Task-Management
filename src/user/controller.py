from fastapi import HTTPException,status,Request
from sqlalchemy.orm import Session
from src.user.dtos import UserSchema,LoginSchema
from src.user.models import UserModel
from pwdlib import PasswordHash
from src.utils.settings import settings
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta

password_hash=PasswordHash.recommended()

def get_hashed_password(password):
    return password_hash.hash(password)

def verify_password(plain_password,hashed_password):
    return password_hash.verify(plain_password,hashed_password)

def register(body:UserSchema,db:Session):
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(400, detail="User already exists")
    
    is_email = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_email:
        raise HTTPException(400, detail="Email already exists")
    
    hashed_password=get_hashed_password(body.password)

    new_user = UserModel(
        username=body.username,
        name=body.name,
        hashed_password=hashed_password,
        email=body.email)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login(body:LoginSchema,db:Session):
    user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User not Found")
    
    if not verify_password(body.password,user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect Password")
    
    exp_time = datetime.now()+timedelta(minutes=settings.EXP_TIME)    
    token = jwt.encode({"_id":user.id,"exp":exp_time},settings.SECRET_KEY,settings.ALGORITHM)

    return {"token":token}

def is_auth(request:Request,db:Session):
    try:
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are Unauthorized")

        token = token.split(" ")[-1]

        data = jwt.decode(token,settings.SECRET_KEY,settings.ALGORITHM)

        user_id = data.get("_id")

        user = db.query(UserModel).filter(UserModel.id == user_id).first()   
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are Unauthorized")

        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are Unauthorized")
    
def get_all_user(db:Session):
    users = db.query(UserModel).all()

    return users

def get_user_by_id(id:int,db:Session):
    user = db.query(UserModel).get(id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    
    return user