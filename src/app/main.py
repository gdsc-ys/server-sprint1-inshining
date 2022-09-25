from fastapi import FastAPI
from api.root_api import  api_router

app = FastAPI()

app.include_router(api_router)