from fastapi import APIRouter, HTTPException, Depends

from schemas.user import UserCreate, User
from config.settings import get_cursor
from services.user import user_service
from psycopg2._psycopg import cursor

router = APIRouter()

@router.post("/", reponse_model=User)
def create_user(obj : UserCreate, cursor : cursor = Depends(get_cursor)):
    user = user_service.get_user_by_username(cursor,username = obj.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="이 유저 네임은 이미 존재합니다"
        )
    user = user_service.create(user_obj = obj)
    return user

