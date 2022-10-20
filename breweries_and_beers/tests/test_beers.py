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
    "name": "Batman Stout",
    "description": "A stout as dark as the dark knight himself!",
    "type": "Stout",
    "ibu": 70,
    "abv": 5.11,
    "brewery": 1,
    "image_url": "https://images.pexels.com/photos/5659755/pexels-photo-5659755.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "category": "Stout",
    "vegetarian_friendly": True,
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