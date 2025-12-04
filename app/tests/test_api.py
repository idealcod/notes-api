from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}

def test_create_note():
    resp = client.post("/notes", params={"text": "hello"})
    assert resp.status_code == 200
    assert "id" in resp.json()

def test_get_notes():
    resp = client.get("/notes")
    assert resp.status_code == 200
    assert "notes" in resp.json()

def test_single_note():
    new = client.post("/notes", params={"text": "test"})
    note_id = new.json()["id"]
    resp = client.get(f"/notes/{note_id}")
    assert resp.status_code == 200
    assert resp.json()["id"] == note_id
