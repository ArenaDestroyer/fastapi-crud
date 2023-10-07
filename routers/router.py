import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from services import service as UserService
from dto import user_model as UserDTO

router = APIRouter()

@router.post("/", tags=["user"])
async def create(data: UserDTO.User = None, db: Session = Depends(get_db)):
    user = UserDTO.User(name=data.name, balance=data.balance, registration_time=data.registration_time)
    return UserService.create_user(user, db)

@router.get("/{id}", tags=["user"])
async def get(id: int = None, db: Session = Depends(get_db)):
    user = UserService.get_user(id, db)
    if user:
        return {"user": user, "registration_time": user.registration_time}
    return {"user": None, "registration_time": None}

@router.put("/{id}", tags=["user"])
async def update(id: int = None, data: UserDTO.User = None, db: Session = Depends(get_db)):
    return UserService.update(data, db, id)

@router.delete("/{id}", tags=["user"])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return UserService.remove(db, id)