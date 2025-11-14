# app/main.py
from typing import Optional

from contextlib import asynccontextmanager
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import engine, SessionLocal
from app.models import Base



from fastapi import FastApi, Depends, HTTPException,status,Response
from app.database import engine, SessionLocal
from app.models import Base,UserDB,projectDB
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session,selectinload
#from app.schemas import 

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup (dev/exam). Prefer Alembic in production.
    Base.metadata.create_all(bind=engine)
    yield



from app.schemas import (
    UserCreate,
    UserRead,
    UserUpdate,
    #course create
    #course read
    ProjectCreate,
    ProjectRead,
    ProjectReadWithOwner,
    ProjectCreateForUser,
    ProjectUpdatefor

)




app = FastAPI(lifespan=lifespan)

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


    def commit_or_rolllback(db:Session,error_msg:str):
        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code = 409, detail=error_msg)


    # ---- Health ----
    @app.get("/health")
    def health():
        return {"status": "ok"}

    @app.post(
        "/api/projects",
        response_model=ProjectRead, status_code=201
    )

    def create_project(project:ProjectCreate, db:Session = Depends(get_db)):
        user = db.get(UserDB, project.owner-id)
        if not user:
            raise HTTPException(status_code=404, detail = "Author Not Found")
        
        proj = projectDB(
            name = project.name,
            description = project.description,
            owner_id = project.owner_id,
        )


@app.get ("/api/users/{user_id}/projects", response_model=list[ProjectRead])
 def get user




    db.add(proj)
    commit_or_rolllback(db,"Book Creation Failed")
    db.refresh(proj)
    return proj


    @app.get ("/api/projects/{project_id}", response_model=ProjectReadWithOwner)

    def get_project_with_owner(project_id:int,
    db:Session = Depends(get_db)):

        stmt = (
            select(projectDB)
            .where(ProjectDB.id==project_id)
            .options(selectinload(ProjectDB.owner))
        )
        
        proj = db.execute(stmt).scalar_one_or_none()
        if not proj:
            raise HTTPException(status_code=404, detail = "BOOK NOT FOUND")
        return proj

    @app.patch ("/api/projects/{project_id}", reponse_ =ProjectRead)
