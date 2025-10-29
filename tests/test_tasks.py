from fastapi.testclient import TestClient
from app.adapters.http.fastapi_app import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_create_and_list_task():
    r = client.post("/tasks", json={"title": "mi tarea", "status": "pending"})
    assert r.status_code == 201
    data = r.json()
    assert data["title"] == "mi tarea"
    assert data["status"] in ("pending", "done")

    r2 = client.get("/tasks")
    assert r2.status_code == 200
    assert any(t["id"] == data["id"] for t in r2.json())
