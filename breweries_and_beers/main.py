from fastapi import FastAPI
from breweries import breweries

app = FastAPI()

app.include_router(breweries.router)