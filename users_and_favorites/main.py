from fastapi import FastAPI
from authenticator import authenticator
from routers import users

app = FastAPI()

app.include_router(users.router)
app.include_router(authenticator.router)
