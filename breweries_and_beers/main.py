from fastapi import FastAPI
from breweries import breweries
from favorites import favorites_router
from fastapi.middleware.cors import CORSMiddleware
from beers import beers
import os
from authenticator import authenticator


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    os.environ.get("CORS_HOST", "REACT_APP_USERS_AND_FAVORITES_API_HOST")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(breweries.router)
app.include_router(favorites_router.router)
app.include_router(beers.router)
app.include_router(authenticator.router)

