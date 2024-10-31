from typing import Annotated
from fastapi import APIRouter, FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from database import SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models import Users
from routers.AuthController import get_current_user


app = FastAPI()

router = APIRouter(
    prefix='/user',
    tags=['user']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
pass_dependency = Annotated[OAuth2PasswordRequestForm, Depends()]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class ChangePasswordRequest(BaseModel):
    old_password: str = Field(min_length=1)
    new_password: str = Field(min_length=1)
    repeat_password: str = Field(min_length=1)

async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    
    db_user = db.query(Users).filter(Users.id == int(user.get('id'))).first()
    
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return db_user


@router.put("/user/{email}", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency, email: str, password_request: ChangePasswordRequest):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    db_user = db.query(Users).filter(Users.id == int(user.get('id'))).first()

    email = db.query(Users).filter(Users.email == db_user.email).first()
    if email is None:
        raise HTTPException(status_code=404, detail='Email not exits')
    
    if not bcrypt_context.verify(password_request.old_password, db_user.hashed_password):
        raise HTTPException(status_code=404, detail='Old password not exits')
    
    if password_request.new_password != password_request.repeat_password :
        raise HTTPException(status_code=401, detail='New password not repeat')
    
    db_user.hashed_password = bcrypt_context.hash(password_request.new_password)

    db.add(db_user)
    db.commit()
    
