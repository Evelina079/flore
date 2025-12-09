from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...db.session import SessionLocal
from ... import crud, schemas

router = APIRouter(prefix="/api/v1/orders", tags=["orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.OrderOut)
def create_order(order_in: schemas.OrderCreate, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email=None)  # not used here
    order = crud.create_order(db, user_id=order_in.user_id, total_price=order_in.total_price, address=order_in.delivery_address)
    return order
