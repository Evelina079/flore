from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Mock Payment/Email Service")

class PaymentRequest(BaseModel):
    user_id: int
    amount: float

class PaymentResponse(BaseModel):
    status: str
    transaction_id: str

@app.post("/payment/", response_model=PaymentResponse)
def mock_payment(data: PaymentRequest):
    # Просто имитируем успешный платёж
    return PaymentResponse(status="success", transaction_id="TX123456")

class EmailRequest(BaseModel):
    to: str
    subject: str
    body: str

@app.post("/email/")
def mock_email(data: EmailRequest):
    # Просто возвращаем, что письмо "отправлено"
    return {"status": "sent", "to": data.to}
