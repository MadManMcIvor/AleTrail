from typing import Literal
from fastapi import APIRouter, Depends, Response
from pydantic import BaseModel

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
    phone: str
    image_url: str
    description: str
    website: str

@router.get("/breweries", response_model=BreweryOut)
def get_breweries(queries: BreweryQueries = Depends()):
    return {"breweries": queries.get_breweries()}