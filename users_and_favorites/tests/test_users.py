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


headers = {
    "Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0MmU3YzBjOC1lZDVlLTQ4ZjUtYTRmNy1iMjg0NzE0ZThjNzciLCJleHAiOjE2NjYzMDczOTcsInN1YiI6Im1hY3lAbWFpbC5jb20iLCJhY2NvdW50Ijp7ImlkIjoxMiwiZmlyc3QiOiJNYWN5IiwibGFzdCI6IlNob3AiLCJwcm9maWxlX3BpYyI6bnVsbCwiZW1haWwiOiJtYWN5QG1haWwuY29tIiwidXNlcm5hbWUiOiJtYWN5IiwiaXNfYnJld2VyeV9vd25lciI6ZmFsc2V9fQ.27gCnpxF6-B7LlQaOGZb8xKEFGjnROCLCSo_rKuAfn4"
}

def test_get_all_users_empty():
    app.dependency_overrides[UserQueries] = TestEmptyUserQueries

    response = client.get('/users', headers = headers)
    assert response.status_code == 200
    assert response.json() == { 'users' : [] }

    app.dependency_overrides = {}

def test_get_all_users():
    app.dependency_overrides[UserQueries] = TestUserQueries
    response = client.get('/users', headers = headers)

    assert response.status_code == 200
    assert response.json() == { 'users' : [user] }


    app.dependency_overrides = {} 

    


    