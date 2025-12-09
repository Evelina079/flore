from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...db.session import SessionLocal
from ... import crud, schemas

router = APIRouter(prefix="/api/v1/bouquets", tags=["bouquets"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.BouquetOut])
def list_bouquets(db: Session = Depends(get_db)):
    return crud.list_bouquets(db)
