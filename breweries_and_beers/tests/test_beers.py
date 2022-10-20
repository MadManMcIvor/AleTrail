from fastapi.testclient import TestClient
import sys
import pathlib
import os
 
fastapi_dir = pathlib.Path(__file__).parent.parent.resolve()
abs_dir = os.path.abspath(fastapi_dir)
sys.path.append(abs_dir)

from main import app
from db import BeerQueries

client = TestClient(app)

class EmptyBeerQueries:
    def get_beers(self):
        return []

class MockBeerQueries:
    def get_beers(self):
        return [beer]

beer = {
    "beer_id": 1,
    "name": "str",
    "description": "str",
    "type": "str",
    "ibu": "str",
    "abv": 0,
    "brewery": "str",
    "image_url": "str",
    "category": "str",
    "vegetarian_friendly": "str",
}

def test_get_beers_empty():
    app.dependency_overrides[BeerQueries] = EmptyBeerQueries

    response = client.get('/beers')

    assert response.status_code == 200
    assert response.json() == { 'beers': [] }

    app.dependency_overrides = {}

def test_get_beers():
    app.dependency_overrides[BeerQueries] = MockBeerQueries

    response = client.get('/beers')

    assert response.status_code == 200
    assert response.json() == { 'beers': [beer] }

    app.dependency_overrides = {}