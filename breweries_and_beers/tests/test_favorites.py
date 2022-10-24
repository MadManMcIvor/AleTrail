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

class MockInvalidTokenBreweryFavoritesQueries:
    def get_all(self):
        return invalid_token_response


invalid_token_response = {
  "detail": "Invalid token"
}

def test_get_breweries_favorites_invalid_token():
    app.dependency_overrides[BreweryFavoritesRepository] = MockInvalidTokenBreweryFavoritesQueries

    response = client.get('/favorites/breweries')
    print(response)

    assert response.status_code == 401
    assert response.json() == invalid_token_response

    app.dependency_overrides = {}
