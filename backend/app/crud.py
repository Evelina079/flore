from sqlalchemy.orm import Session
from . import models, core

# ---------------------- Пользователи ----------------------
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, name: str, email: str, password: str):
    if get_user_by_email(db, email):
        raise ValueError("Пользователь с таким email уже существует")
    hashed = core.security.get_password_hash(password)
    user = models.User(name=name, email=email, password_hash=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def list_users(db: Session):
    return db.query(models.User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).get(user_id)

# ---------------------- Букеты ----------------------
def create_bouquet(db: Session, name: str, price: float, description: str = ""):
    if db.query(models.Bouquet).filter(models.Bouquet.name == name).first():
        raise ValueError("Букет с таким именем уже существует")
    b = models.Bouquet(name=name, price=price, description=description)
    db.add(b)
    db.commit()
    db.refresh(b)
    return b

def list_bouquets(db: Session):
    return db.query(models.Bouquet).all()

def get_bouquet_by_id(db: Session, bouquet_id: int):
    return db.query(models.Bouquet).get(bouquet_id)

# ---------------------- Заказы ----------------------
def create_order(db: Session, user_id: int, total_price: float, address: str):
    user = get_user_by_id(db, user_id)
    if not user:
        raise ValueError("Пользователь не найден")
    o = models.Order(user_id=user_id, total_price=total_price, delivery_address=address)
    db.add(o)
    db.commit()
    db.refresh(o)
    return o

def list_orders(db: Session):
    return db.query(models.Order).all()

def get_order_by_id(db: Session, order_id: int):
    return db.query(models.Order).get(order_id)
