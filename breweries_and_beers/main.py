from fastapi import FastAPI
import breweries
from favorites import favorites_router
from fastapi.middleware.cors import CORSMiddleware
import beers

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
app.include_router(favorites_router.router)
app.include_router(beers.router)
