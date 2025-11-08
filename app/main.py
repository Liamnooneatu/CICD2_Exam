# app/main.py
from typing import Optional

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import engine, SessionLocal
from app.models import Base
#from app.schemas import 

app = FastAPI(title="Authors & Books API")
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()

# ---- Health ----
@app.get("/health")
def health():
    return {"status": "ok"}

