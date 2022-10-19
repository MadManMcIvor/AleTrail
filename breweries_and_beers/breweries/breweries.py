from fastapi import APIRouter, Depends, Response
from pydantic import BaseModel
from typing import Optional
from authenticator import authenticator

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

@router.get("/brewery/{brewery_id}", response_model=BreweryOut)
def get_brewery(
    brewery_id: int,
    response: Response,
    queries: BreweryQueries = Depends(),
    ):
    record = queries.get_brewery(brewery_id)
    if record is None:
        response.status_code = 404
    else:
        return record

@router.get("/breweries", response_model=BreweriesOut)
def get_breweries(queries: BreweryQueries = Depends()):
    return {"breweries": queries.get_breweries()}

@router.get("/breweries/{city}", response_model=BreweriesOut)
def get_breweries_by_city(
    city: str,
    response: Response,
    queries: BreweryQueries = Depends()
    ):
    record = queries.get_breweries_by_city(city)
    if record is None:
        response.status_code = 404
    else:
        return {"breweries": record}

@router.post("/breweries", response_model=BreweryOut)
def create_brewery(
    brewery: BreweryIn, 
    queries: BreweryQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data), 
):
    if account_data:
        return queries.create_brewery(brewery)


@router.put("/brewery/{brewery_id}", response_model=BreweryOut)
def update_brewery(
    brewery_id: int,
    brewery_in: BreweryIn,
    response: Response,
    queries: BreweryQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    if account_data:
        record = queries.update_brewery(brewery_id, brewery_in)
        if record is None:
            response.status_code = 404
        else:
            return record


@router.delete("/brewery/{brewery_id}", response_model=bool)
def delete_brewery(
    brewery_id: int, 
    queries: BreweryQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    if account_data:
        queries.delete_brewery(brewery_id)
        return True

