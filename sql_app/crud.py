from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_apis(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.API).offset(skip).limit(limit).all()


def create_user_api(db: Session, api: schemas.APICreate, user_id: int):
    db_api = models.API(**api.dict(), owner_id=user_id)
    db.add(db_api)
    db.commit()
    db.refresh(db_api)
    return db_api
