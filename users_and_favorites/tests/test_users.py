from fastapi.testclient import TestClient

import sys
import pathlib
import os

fastapi_dir = pathlib.Path(__file__).parent.parent.resolve()
abs_dir = os.path.abspath(fastapi_dir)
sys.path.append(abs_dir)

from main import app
from queries.users import UserQueries
from authenticator import authenticator

client = TestClient(app)


class TestUserQueries:
    def get_all_users(self):
        return [testUser]

testUser = {
  "id": 1,
  "first": "test",
  "last": "test",
  "profile_pic": "",
  "email": "email@test.com",
  "username": "test"
}


def user_override():
  return testUser 


def test_get_all_users():
    app.dependency_overrides[UserQueries] = TestUserQueries
    app.dependency_overrides[authenticator.try_get_current_account_data] = user_override
    response = client.get('/users')

    assert response.status_code == 200
    assert response.json() ==  { 'users' : [testUser] }

    app.dependency_overrides = {}


class TestInvalidTokenUserQueries:
    def get_all_users(self):
        return invalid_token

invalid_token = {
  "detail": "Invalid token"
}

def test_get_all_users_invalid_token():
    app.dependency_overrides[UserQueries] = TestInvalidTokenUserQueries

    response = client.get('/users')

    assert response.status_code == 401
    assert response.json() == invalid_token

    app.dependency_overrides = {} 


