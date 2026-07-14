from app import app

client = app.test_client()

def test_home():
    response = client.get("/items")
    assert response.status_code == 200

def test_get_item():
    response = client.get("/items/1")
    assert response.status_code == 200

def test_add_item():
    response = client.post("/items", json={
        "barcode": "3017620422003",
        "quantity": 5,
        "price": 500
    })

    assert response.status_code == 201

def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 204