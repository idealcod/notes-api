from fastapi import FastAPI
from app.db import get_conn
from app.models import CREATE_NOTES_TABLE

app = FastAPI()

# Создаём таблицу при старте
conn = get_conn()
cur = conn.cursor()
cur.execute(CREATE_NOTES_TABLE)
conn.commit()
cur.close()
conn.close()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/notes")
def create_note(text: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO notes(text) VALUES (%s) RETURNING id", (text,))
    note_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"id": note_id, "text": text}

@app.get("/notes")
def get_notes():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, text FROM notes")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return {"notes": [{"id": r[0], "text": r[1]} for r in rows]}

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, text FROM notes WHERE id=%s", (note_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return {"id": row[0], "text": row[1]}
    return {"error": "Not found"}
