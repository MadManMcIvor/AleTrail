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
    APIRouter,
)

router = APIRouter()


@router.post("/favorites/breweries", response_model=BreweryFavoriteOut)
def create_brewery_favorite(
    brewery_favorite: BreweryFavoriteIn, repo: BreweryFavoritesRepository = Depends()
):
    return repo.create(brewery_favorite)


@router.get("/favorites/breweries", response_model=List[BreweryFavoriteJoinOut])
def get_all_brewery_favorites_by_user(
    repo: BreweryFavoritesRepository = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    user_id = account_data["id"]
    return repo.get_all(user_id)


@router.delete("/favorites/breweries/{brewery_favorite_id}", response_model=bool)
def delete_brewery_favorite(
    brewery_favorite_id: int,
    repo: BreweryFavoritesRepository = Depends(),
) -> bool:
    return repo.delete(brewery_favorite_id)


@router.post("/favorites/beers", response_model=BeerFavoriteOut)
def create_beer_favorite(
    beer_favorite: BeerFavoriteIn, repo: BeerFavoritesRepository = Depends()
):
    return repo.create(beer_favorite)


@router.get("/favorites/beers", response_model=List[BeerFavoriteJoinOut])
def get_all_beer_favorites_by_user(
    repo: BeerFavoritesRepository = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    user_id = account_data["id"]
    return repo.get_all(user_id)


@router.delete("/favorites/beers/{beer_favorite_id}", response_model=bool)
def delete_beer_favorite(
    beer_favorite_id: int,
    repo: BeerFavoritesRepository = Depends(),
) -> bool:
    return repo.delete(beer_favorite_id)
