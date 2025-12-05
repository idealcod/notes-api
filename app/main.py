from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.db import get_conn

app = FastAPI()

class NoteCreate(BaseModel):
    text: str

@app.get("/health")
def healthcheck():
    return {"status": "ok"}

@app.post("/notes")
def create_note(note: NoteCreate):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO notes (text) VALUES (%s) RETURNING id, text;",
        (note.text,)
    )
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return {"id": result[0], "text": result[1]}

@app.get("/notes")
def get_notes():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, text FROM notes;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return {"notes": [{"id": r[0], "text": r[1]} for r in rows]}

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, text FROM notes WHERE id = %s;", (note_id,))
    row = cur.fetchone()
    cur.close()

    if not row:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"id": row[0], "text": row[1]}

@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteCreate):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "UPDATE notes SET text = %s WHERE id = %s RETURNING id, text;",
        (note.text, note_id)
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()

    if not row:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"id": row[0], "text": row[1]}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM notes WHERE id = %s RETURNING id;", (note_id,))
    row = cur.fetchone()
    conn.commit()
    cur.close()

    if not row:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"status": "deleted", "id": note_id}
