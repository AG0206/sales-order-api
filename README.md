# Sales Order API 🚀

A professional FastAPI-based Sales Order Management System with Pydantic models, business logic validation, and comprehensive pytest testing.

## Project Structure

```
sales_order_app/
├── main.py              # FastAPI application with all endpoints
├── models.py            # Pydantic data models with validation
├── data.py              # In-memory data storage
├── logic.py             # Business logic (status workflow)
├── test_main.py         # Unit tests (5 tests)
├── requirements.txt     # Python dependencies
└── README.md            # Documentation
```

## Setup Instructions

### 1. Clone/Download Project
```bash
cd sales_order_app
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the API

Start the development server:
```bash
uvicorn main:app --reload
```

Access the API:
- **Swagger UI (Interactive):** http://127.0.0.1:8000/docs
- **ReDoc (Documentation):** http://127.0.0.1:8000/redoc

## API Endpoints

### Customers
- `POST /customers` - Create customer
- `GET /customers` - List all customers

### Items
- `POST /items` - Create item
- `GET /items` - List all items

### Orders
- `POST /orders` - Create order (calculates total automatically)
- `GET /orders` - List all orders
- `GET /orders/{order_id}` - Get specific order
- `PUT /orders/{order_id}/status` - Update order status

## Status Workflow

Valid transitions:
```
Draft → Submitted
Draft → Cancelled
Submitted → Cancelled
```

Invalid transitions will return HTTP 400 error.

## Running Tests

```bash
pytest
```

Expected output: **5 passed** ✅

### Test Coverage
1. ✅ Home endpoint
2. ✅ Customer creation
3. ✅ Item creation
4. ✅ Order creation with automatic total calculation
5. ✅ Invalid status flow validation

## Features

- **✅ Customer Management** - Create and list customers
- **✅ Item Catalog** - Manage inventory items with prices
- **✅ Sales Orders** - Create orders with automatic total calculation
- **✅ Status Workflow** - Validated state machine (Draft → Submitted → Cancelled)
- **✅ Pydantic Validation** - Type checking and constraints (quantity > 0)
- **✅ Error Handling** - Proper HTTP error responses with meaningful messages
- **✅ Comprehensive Testing** - 5 unit tests with pytest

## Sample API Usage

### Create Customer
```json
POST /customers
{
  "id": 1,
  "name": "Aarti",
  "email": "aarti@gmail.com"
}
```

### Create Item
```json
POST /items
{
  "id": 1,
  "name": "Laptop",
  "price": 50000
}
```

### Create Order
```json
POST /orders
{
  "id": 1,
  "customer_id": 1,
  "items": [
    {
      "item_id": 1,
      "quantity": 2
    }
  ]
}
```
Response: Total automatically calculated as `100000` (50000 × 2)

### Update Order Status
```
PUT /orders/1/status?new_status=Submitted
```

## Project Completion Checklist

- ✅ STEP 1: Project setup with venv
- ✅ STEP 2: File structure created
- ✅ STEP 3: Pydantic models with validation
- ✅ STEP 4: In-memory data storage
- ✅ STEP 5: Business logic (status workflow)
- ✅ STEP 6: Main FastAPI application
- ✅ STEP 8: Customer APIs
- ✅ STEP 9: Item APIs
- ✅ STEP 10: Order total calculation
- ✅ STEP 11: Order creation API
- ✅ STEP 12: Order retrieval APIs
- ✅ STEP 13: Order status update API
- ✅ STEP 14: Enhanced validation with Field constraints
- ✅ STEP 15: Duplicate order ID check
- ✅ STEP 17: Testing tools installed
- ✅ STEP 18-23: 5 comprehensive tests
- ✅ STEP 24: All tests passing
- ✅ requirements.txt created
- ✅ README.md documented
