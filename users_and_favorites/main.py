from fastapi import FastAPI
from authenticator import authenticator
from routers import users, favorites_router

app = FastAPI()

app.include_router(users.router)
app.include_router(favorites_router.router)
app.include_router(authenticator.router)
