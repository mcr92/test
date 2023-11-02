from fastapi import FastAPI, Body
from model import Orders
from typing import List
from decimal import Decimal
from utils import criterion_choice

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/solution")
def process_orders(orders: List[Orders], criterion:criterion_choice=Body())->Decimal:
    revenue = 0
    if criterion=="all":
        for element in orders:
            revenue += element.quantity * element.price
        return round(revenue, 2)
    else:
        for element in orders:
            if element.status == criterion:
                revenue += element.quantity * element.price
        return round(revenue, 2)