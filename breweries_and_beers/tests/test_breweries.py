from fastapi.testclient import TestClient
import sys
import pathlib
import os
 
fastapi_dir = pathlib.Path(__file__).parent.parent.resolve()
abs_dir = os.path.abspath(fastapi_dir)
sys.path.append(abs_dir)

from main import app
from db import BreweryQueries

client = TestClient(app)

class MockEmptyBreweryQueries:
    def get_breweries(self):
        return []

class MockBreweryQueries:
    def get_breweries(self):
        return [brewery]

brewery = {
    "brewery_id": 1,
    "name": "str",
    "street": "str",
    "city": "str",
    "state": "str",
    "zip_code": 0,
    "phone": "str",
    "image_url": "str",
    "description": "str",
    "website": "str",
}

def test_get_breweries_empty():
    app.dependency_overrides[BreweryQueries] = MockEmptyBreweryQueries

    response = client.get('/breweries')

    assert response.status_code == 200
    assert response.json() == { 'breweries': [] }

    app.dependency_overrides = {}

def test_get_breweries():
    app.dependency_overrides[BreweryQueries] = MockBreweryQueries

    response = client.get('/breweries')

    assert response.status_code == 200
    assert response.json() == { 'breweries': [brewery] }

    app.dependency_overrides = {}