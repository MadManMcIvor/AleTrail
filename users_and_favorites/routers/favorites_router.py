from urllib import response
from queries.favorites_queries import ( BreweryFavoriteIn,
BeerFavoriteIn,
)
from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)

router = APIRouter()

@router.post("/favorites/beers")
def create_brewery_favorite(brewery_favorite: BreweryFavoriteIn):
    return brewery_favorite