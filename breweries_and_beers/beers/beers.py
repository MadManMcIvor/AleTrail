from pydantic import BaseModel
from fastapi import APIRouter, Depends, Response
from db import BeerQueries

router = APIRouter()

class BeerIn(BaseModel):
    name: str
    description: str
    type: str
    ibu: str
    abv: str
    website: str
    brewery: str
    image_url: str
    category: str
    vegetarian_friendly: bool
    owner_id: int

class BeerOut(BaseModel):
    id: int
    name: str
    description: str
    type: str
    ibu: str
    abv: str
    website: str
    brewery: str
    image_url: str
    category: str
    vegetarian_friendly: bool
    owner_id: int

class BeerList(BaseModel):
    beers: list[BeerOut]

# class BeerDelete(BaseModel):
#     result: bool

@router.get("/beers", response_model=BeerOut)
def get_beers(queries: BeerQueries = Depends()):
    return {"beers": queries.get_beers()}

@router.post("/beers", response_model=BeerOut)
def create_beer(beer: BeerIn, queries: BeerQueries = Depends()):
    return queries.create_beer(beer)