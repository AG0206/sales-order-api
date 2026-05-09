from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Sales Order API Running"


def test_create_customer():
    response = client.post(
        "/customers",
        json={
            "id": 1,
            "name": "Aarti",
            "email": "aarti@gmail.com"
        }
    )
    assert response.status_code == 200


def test_create_item():
    response = client.post(
        "/items",
        json={
            "id": 1,
            "name": "Laptop",
            "price": 50000
        }
    )
    assert response.status_code == 200


def test_create_order():
    response = client.post(
        "/orders",
        json={
            "id": 1,
            "customer_id": 1,
            "items": [
                {
                    "item_id": 1,
                    "quantity": 2
                }
            ]
        }
    )
    data = response.json()
    assert response.status_code == 200
    assert data["data"]["total"] == 100000


def test_invalid_status_flow():
    # submit order
    client.put("/orders/1/status?new_status=Submitted")
    # cancel order
    client.put("/orders/1/status?new_status=Cancelled")
    # try invalid rollback
    response = client.put(
        "/orders/1/status?new_status=Submitted"
    )
    assert response.status_code == 400
