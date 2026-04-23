from fastapi import FastAPI
import sqlite3
from fastapi.middleware.cors import CORSMiddleware
import os

from pydantic import BaseModel

app = FastAPI(title="User Registry")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserCreate(BaseModel):
    name: str
    age: int
    height: int

@app.post("/users")
def add_user(user: UserCreate):
    conn = sqlite3.connect("../db/data.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, age, height) VALUES (?, ?, ?)", (user.name, user.age, user.height))
    conn.commit()

    conn.close()

    return {
        "done": "done"
    }

@app.get("/users")
def fetch_users():
    conn = sqlite3.connect("../db/data.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    users = [ row for row in cur.fetchall()]

    conn.close()

    return {
        "users": users
    }
    
