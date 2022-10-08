from fastapi import APIRouter
from api import boards, comments

api_router = APIRouter()
api_router.include_router(boards.router, prefix="/boards")
api_router.include_router(comments.router, prefix="/comments")