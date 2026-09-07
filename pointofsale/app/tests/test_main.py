from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    url = "/" ## arrange the inputs 
    response = client.get(url) # act by calling the endpoint
    # print (response.json())
    # print(response.status_code)
    assert response.status_code == 200 # assert the expected output
    assert response.json() == {"message": "Welcome to the Point of Sale API!"}

    #pytest tests/main.py

    