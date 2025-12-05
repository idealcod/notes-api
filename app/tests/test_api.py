import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db import get_conn

client = TestClient(app)

# ------------------------
# Mocked test (не требует базы)
# ------------------------
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# ------------------------
# Integration tests (с реальной базой)
# ------------------------
@pytest.fixture(scope="module")
def db_connection():
    conn = get_conn()
    yield conn
    conn.close()

def test_create_note_real(db_connection):
    payload = {"text": "Интеграционная заметка"}
    response = client.post("/notes", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["text"] == payload["text"]

def test_get_notes_real(db_connection):
    response = client.get("/notes")
    assert response.status_code == 200
    data = response.json()
    assert "notes" in data
    assert isinstance(data["notes"], list)
