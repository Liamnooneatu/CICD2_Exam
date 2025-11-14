import pytest
from fastapi.testclient import Test_Client
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app, get_db
from app.models import Base

TEST_DB_URL="sqlite+pysqlite:///:memory"

engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread":False}, poolclass = StaticPool)

TestingSessionLocal = sessionmaker(bind=engine , expire_on_commit=False)

Base.metadata.create_all(bind=engine)

@pytest.fixture
def clients:
def override_get_db():
    db=TestingSessionLocal()
    try:
            yield db
    finally: 
            db.close
    app.dependency_overrides[get_db]=override_get_db
    with Test_Client(app) as c:
           yield c

def test_patch_user_partial_update_success(client):
       create=client.post(
       "/api/users", 
       json = {"name": "Liam", "email": "Liam@atu.com", "age" : 30, "student_d" : "s1234567"},
       )

    assert create.status_code==200, r.text
    body = r.json()
    assert body ["id"]==["id"]
    assert body ["name"]=="liam updated"
    assert body ["email"]=="liam@atu.com"
    assert body ["student_id"]=="s1234567"

def test_put_user_full_update_success(client):
        create=client.post(
        "/api/users",
        json = {"name": "John", "email": "John@atu.ie", "age" : 25, "student_id": "s7654321"},
        )
        assert create.status_code==200, r.text
        body = r.json()

    payload = {
        "name" : "Mike",
        "email" : "Mike@atu.ie",
        "age": 29,
        "student_id" : "s4444444"
    }


r = client.put(f"/api/users/{u['id']}"json = payload)


def test_put_user_not_found(client):
       payload = {
              "name" : "ghost",
              "email" : "ghost@atu.ie",
              "age" : 30,
              "student_id" : "s3333333"
       }
       r = client.put("/api/users/424242", json = payload)
       assert r.status_code == 404
       assert r.json()["detail"] == "Author not found"


def _create_owner(client, name= "owner", emial="owner@atu.ie", age = 28, id = "s5555555"):
       
       r = client.post(
              "/api/users"
              json = {"name":name, "email": email, "age": age, "studdent_id":sid}
       )
       assert r.status_code == 201, r.text
       assert r.json()

def create_project(client):
       r= client.post("/api/projects", json= {"name": "cicd2", "description": "Author book project", "owner_id": "1"},
       )
       assert r.status_code in (200,201)


def test_create_project(client):
       owner = _create_owner(client)
       r = client.post(
              "/api/projects",
              json = {"name": "Book Program", "description" : "saves authors names", "owner_id" : ["id"]}              
       )

       assert r.status_code in (200,201), r.text