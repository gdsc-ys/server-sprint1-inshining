from fastapi import APIRouter
from api import boards

api_router = APIRouter()
api_router.include_router(boards.router, prefix="/boards")