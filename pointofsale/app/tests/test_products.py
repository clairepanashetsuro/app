from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == []

    #pytest tests/test_products.py
    
def test_create_product():
    product_data = {
        "name": "Test Product",
        "description": "This is a test product.",
        "price": 9.99,
        "quantity": 10
    }
    response = client.post("/products", json=product_data)
    assert response.status_code == 201
    assert response.json()["name"] == product_data["name"]
    assert response.json()["description"] == product_data["description"]
    assert response.json()["price"] == product_data["price"]
    assert response.json()["quantity"] == product_data["quantity"]