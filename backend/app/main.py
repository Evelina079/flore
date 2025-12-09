from fastapi import FastAPI
from .db import base
from .db.session import engine
from .api.v1 import auth, bouquets, orders

# Создаём таблицы (для простого старта; в prod — alembic)
base.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Flore API")

app.include_router(auth.router)
app.include_router(bouquets.router)
app.include_router(orders.router)

@app.get("/")
def root():
    return {"status": "ok"}
