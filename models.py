from pydantic import BaseModel, Field
from typing import List


class Customer(BaseModel):
    id: int
    name: str
    email: str


class Item(BaseModel):
    id: int
    name: str
    price: float


class OrderItem(BaseModel):
    item_id: int
    quantity: int = Field(gt=0)


class SalesOrder(BaseModel):
    id: int
    customer_id: int
    items: List[OrderItem]
    status: str = "Draft"
    total: float = 0
