from typing import Literal
from fastapi import APIRouter, Depends, Response
from pydantic import BaseModel
from typing import Optional

from db import BreweryQueries


router = APIRouter()

class BreweryIn(BaseModel):
    name: str
    street: str
    city: str
    state: str
    zip_code: int
    phone: str
    image_url: str
    description: str
    website: str

class BreweryOut(BaseModel):
    brewery_id: int
    name: str
    street: str
    city: str
    state: str
    zip_code: int
    phone: Optional[str]
    image_url: Optional[str]
    description: Optional[str]
    website: Optional[str]

class BreweriesOut(BaseModel):
    breweries: list[BreweryOut]

@router.get("/breweries", response_model=BreweriesOut)
def get_breweries(queries: BreweryQueries = Depends()):
    return {"breweries": queries.get_breweries()}

# @router.post("/breweries", response_model=BreweryOut)
# def create_brewery(
#     brewery: BreweryIn, 
#     queries: BreweryQueries = Depends(), 
# ):
#     return queries.create_brewery(brewery)
