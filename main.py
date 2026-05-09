from fastapi import FastAPI, HTTPException
from models import Customer, Item, SalesOrder, OrderItem
from data import customers, items, orders
from logic import is_valid_status_change

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Sales Order API Running"}


def calculate_order_total(order_items):
    total = 0
    for order_item in order_items:
        item_found = None
        for item in items:
            if item.id == order_item.item_id:
                item_found = item
                break
        if not item_found:
            raise HTTPException(
                status_code=404,
                detail=f"Item with ID {order_item.item_id} not found"
            )
        total += item_found.price * order_item.quantity
    return total


# CREATE CUSTOMER
@app.post("/customers")
def create_customer(customer: Customer):
    # check duplicate id
    for c in customers:
        if c.id == customer.id:
            raise HTTPException(status_code=400, detail="Customer ID already exists")
    customers.append(customer)
    return {
        "message": "Customer created",
        "data": customer
    }


# LIST CUSTOMERS
@app.get("/customers")
def get_customers():
    return customers


# CREATE ITEM
@app.post("/items")
def create_item(item: Item):
    for i in items:
        if i.id == item.id:
            raise HTTPException(status_code=400, detail="Item ID already exists")
    items.append(item)
    return {
        "message": "Item created",
        "data": item
    }


# LIST ITEMS
@app.get("/items")
def get_items():
    return items


# CREATE ORDER
@app.post("/orders")
def create_order(order: SalesOrder):
    # validate customer
    customer_exists = False
    for customer in customers:
        if customer.id == order.customer_id:
            customer_exists = True
            break
    if not customer_exists:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    
    # check duplicate order id
    for existing_order in orders:
        if existing_order.id == order.id:
            raise HTTPException(
                status_code=400,
                detail="Order ID already exists"
            )
    
    # calculate total
    order.total = calculate_order_total(order.items)
    orders.append(order)
    return {
        "message": "Order created",
        "data": order
    }


# LIST ORDERS
@app.get("/orders")
def get_orders():
    return orders


# GET ORDER BY ID
@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders:
        if order.id == order_id:
            return order
    raise HTTPException(
        status_code=404,
        detail="Order not found"
    )


# UPDATE ORDER STATUS
@app.put("/orders/{order_id}/status")
def update_order_status(order_id: int, new_status: str):
    # find order
    order_found = None
    for order in orders:
        if order.id == order_id:
            order_found = order
            break
    
    # order not found
    if not order_found:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )
    
    # valid statuses
    valid_statuses = ["Draft", "Submitted", "Cancelled"]
    if new_status not in valid_statuses:
        raise HTTPException(
            status_code=400,
            detail="Invalid status"
        )
    
    # validate transition
    if not is_valid_status_change(order_found.status, new_status):
        raise HTTPException(
            status_code=400,
            detail=f"Cannot change status from {order_found.status} to {new_status}"
        )
    
    # update status
    order_found.status = new_status
    return {
        "message": "Status updated",
        "data": order_found
    }
