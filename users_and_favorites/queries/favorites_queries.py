from pydantic import BaseModel
from queries.pool import pool

class BreweryFavoriteIn(BaseModel):
    user_id: int
    brewery_id: int

class BeerFavoriteIn(BaseModel):
    id: int
    user_id: int
    beer_id: int

class BreweryFavoritesRepository:
    def create(brewery_favorite: BreweryFavoriteIn):
        pass
