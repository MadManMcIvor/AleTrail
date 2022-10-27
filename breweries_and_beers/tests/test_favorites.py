from fastapi.testclient import TestClient
import sys
import pathlib
import os
 
fastapi_dir = pathlib.Path(__file__).parent.parent.resolve()
abs_dir = os.path.abspath(fastapi_dir)
sys.path.append(abs_dir)

from main import app
from favorites.favorites_queries import BreweryFavoritesRepository
from authenticator import authenticator


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

    assert response.status_code == 401
    assert response.json() == invalid_token_response

    app.dependency_overrides = {}


class MockBreweryFavoritesQueries:
  def get_all(self, user_id):
      return [brewery_favorite]

brewery_favorite =  {
    "brewery_favorite_id": 0,
    "user_id": 0,
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


mock_user = {
  "id": 0,
  "first": "string",
  "last": "string",
  "profile_pic": "string",
  "email": "string",
  "username": "string"
}

def account_override():
    return mock_user


def test_get_breweries_favorites_by_user():
  app.dependency_overrides[BreweryFavoritesRepository] = MockBreweryFavoritesQueries
  app.dependency_overrides[authenticator.try_get_current_account_data] = account_override

  response = client.get('/favorites/breweries')

  assert response.status_code == 200
  assert response.json() == [brewery_favorite]

  app.dependency_overrides = {}

