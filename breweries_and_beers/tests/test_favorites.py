from fastapi.testclient import TestClient
import sys
import pathlib
import os
 
fastapi_dir = pathlib.Path(__file__).parent.parent.resolve()
abs_dir = os.path.abspath(fastapi_dir)
sys.path.append(abs_dir)

from main import app
from favorites.favorites_queries import BreweryFavoritesRepository

client = TestClient(app)

class MockEmptyBreweryFavoritesQueries:
    def get_breweries(self):
        return []

class MockBreweryFavoritesQueries:
    def get_breweries(self):
        return [brewery_favorite]

brewery_favorite = {
    "brewery_favorite_id": 1,
    "user_id": 1,
    "brewery_id": 0,
    "name": "string",
    "street": "string",
    "city": "string",
    "state": "string",
    "zip_code": 0,
    "phone": "string",
    "image_url": "string",
    "description": "string",
    "website": "string"
  }

def test_get_breweries__favorites_empty():
    app.dependency_overrides[BreweryFavoritesRepository] = MockEmptyBreweryFavoritesQueries

    response = client.get('/favorites/breweries')

    assert response.status_code == 200
    assert response.json() == {[]}

    app.dependency_overrides = {}

def test_get_breweries_favorites():
    app.dependency_overrides[BreweryFavoritesRepository] = MockBreweryFavoritesQueries

    response = client.get('/favorites/breweries')

    assert response.status_code == 200
    assert response.json() == { [brewery_favorite] }

    app.dependency_overrides = {}