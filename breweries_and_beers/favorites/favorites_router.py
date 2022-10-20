from urllib import response
from typing import List
from authenticator import authenticator
from favorites.favorites_queries import (
    BreweryFavoriteIn, 
    BreweryFavoriteOut,
    BreweryFavoritesRepository,
    BreweryFavoriteJoinOut,
    BeerFavoriteIn,
    BeerFavoriteOut, 
    BeerFavoritesRepository,
    BeerFavoriteJoinOut,
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

@router.post("/favorites/breweries", response_model=BreweryFavoriteOut)
def create_brewery_favorite(
    brewery_favorite: BreweryFavoriteIn,
    repo: BreweryFavoritesRepository = Depends()
    ):
    return repo.create(brewery_favorite)

@router.get("/favorites/breweries", response_model=List[BreweryFavoriteJoinOut])
def get_all_brewery_favorites_by_user(
    repo: BreweryFavoritesRepository = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):    
    user_id= account_data['id']
    return repo.get_all(user_id)

@router.post("/favorites/beers", response_model=BeerFavoriteOut)
def create_beer_favorite(
    beer_favorite: BeerFavoriteIn,
    repo: BeerFavoritesRepository = Depends()
    ):
    return repo.create(beer_favorite)