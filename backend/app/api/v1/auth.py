from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from ...db.session import SessionLocal
from ... import crud, schemas

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Модель для регистрации
@router.post("/register", status_code=201, response_model=schemas.UserOut)
def register(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = crud.create_user(db, user_in.name, user_in.email, user_in.password)
    return user

# Модель для входа
class UserLogin(BaseModel):
    email: EmailStr
    password: str

@router.post("/login", response_model=schemas.Token)
def login(form_data: UserLogin, db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.email, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    # создаём токен (можно использовать jwt)
    access_token = "some_jwt_token"
    return {"access_token": access_token, "token_type": "bearer"}
