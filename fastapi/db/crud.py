from sqlalchemy.orm import Session
from .models import User
from typing import List, Optional


def get_user_by_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()


def list_all_users(db: Session) -> List[User]:
    return db.query(User).all()
