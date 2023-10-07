from models.models import User
from sqlalchemy.orm import Session
from dto import user_model

def get_all_users(db: Session):
        return db.query(User).all()

def create_user(data: user_model.User, db: Session):
    user = User(name=data.name, balance=data.balance)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    
    return user

def get_user(id: int, db):
    return db.query(User).filter(User.id==id).first()
    
def update(data: user_model.User, db: Session, id: int):
    user = db.query(User).filter(User.id==id).first()
    user.name = data.name
    user.balance = data.balance
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def remove(db: Session, id: int):
    user = db.query(User).filter(User.id==id).delete()
    db.commit()
    return user