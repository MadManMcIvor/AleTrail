from fastapi import FastAPI
from breweries import breweries
from fastapi.middleware.cors import CORSMiddleware
from beers import beers

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(breweries.router)
app.include_router(beers.router)