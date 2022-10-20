from fastapi.testclient import TestClient

import sys
import pathlib
import os

fastapi_dir = pathlib.Path(__file__).parent.parent.resolve()
abs_dir = os.path.abspath(fastapi_dir)
sys.path.append(abs_dir)

from main import app
from queries.users import UserQueries

client = TestClient(app)

class TestEmptyUserQueries:
    def get_all_users(self):
        return []

class TestUserQueries:
    def get_all_users(self):
        return [user]

user = {
  "id": 1,
  "first": "test",
  "last": "str",
  "profile_pic": "",
  "email": "email@test.com",
  "username": "test"
}

token = {
    "access_token" : "hellocodersabcdefghijklmnopqrstuvwqyz12345678910",
    "token_type": "Bearer",
    "user": user 

}

def test_get_all_users_empty():
    app.dependency_overrides[UserQueries] = TestEmptyUserQueries

    response = client.get('/users')

    assert response.status_code == 200
    assert response.json() == { 'users' : [] }

    app.dependency_overrides = {}

def test_get_all_users():
    app.dependency_overrides[UserQueries] = TestUserQueries
    response = client.get('/users')

    assert response.status_code == 200
    assert response.json() == { 'users': [user] }

    app.dependency_overrides = {} 

    


    