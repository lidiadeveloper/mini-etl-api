from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_add_item_and_duplicate():
    # 1. Añadir un producto nuevo
    r = client.post("/items", json={"id": 99, "name": "Bolso", "price": 49.9})
    assert r.status_code == 200
    data = r.json()
    assert data["message"] == "ok"
    assert data["count"] >= 4  # debe haber al menos 4 items

    # 2. Intentar añadir el mismo id otra vez
    r2 = client.post("/items", json={"id": 99, "name": "Bolso", "price": 49.9})
    assert r2.status_code == 200
    data2 = r2.json()
    assert "error" in data2
    assert data2["error"] == "id ya existe"


def test_filter_items_by_price():
    # Filtro con max_price=20 (solo debe devolver productos baratos)
    r = client.get("/items?max_price=20")
    assert r.status_code == 200
    data = r.json()
    assert data["count"] >= 1
    for item in data["items"]:
        assert item["price"] <= 20
