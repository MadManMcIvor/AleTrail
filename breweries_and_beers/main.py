from fastapi import FastAPI
from breweries import breweries
from beers import beers

app = FastAPI()

app.include_router(breweries.router)
app.include_router(beers.router)