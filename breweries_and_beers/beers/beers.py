from pydantic import BaseModel
from fastapi import APIRouter, Depends, Response
from db import BeerQueries
from typing import Optional

router = APIRouter()


class BeerIn(BaseModel):
    name: str
    description: Optional[str]
    type: str
    ibu: int
    abv: float
    brewery: int
    image_url: Optional[str]
    category: Optional[str]
    vegetarian_friendly: Optional[bool]


class BeerOut(BaseModel):
    beer_id: int
    name: str
    description: Optional[str]
    type: str
    ibu: int
    abv: float
    brewery: int
    image_url: Optional[str]
    category: Optional[str]
    vegetarian_friendly: Optional[bool]


class BeerList(BaseModel):
    beers: list[BeerOut]


@router.get("/beers", response_model=BeerList)
def get_beers(queries: BeerQueries = Depends()):
    return {"beers": queries.get_beers()}


@router.get("/beer/{beer_id}", response_model=BeerOut)
def get_beer(beer_id: int, response: Response, queries: BeerQueries = Depends()):
    record = queries.get_beer(beer_id)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.post("/beers", response_model=BeerOut)
def create_beer(beer: BeerIn, queries: BeerQueries = Depends()):
    return queries.create_beer(beer)


@router.put("/beer/{beer_id}", response_model=BeerOut)
def update_beer(
    beer_id: int,
    beer_in: BeerIn,
    response: Response,
    queries: BeerQueries = Depends(),
):
    record = queries.update_beer(beer_id, beer_in)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.delete("/beer/{beer_id}", response_model=bool)
def delete_beer(beer_id: int, queries: BeerQueries = Depends()):
    queries.delete_beer(beer_id)
    return True
