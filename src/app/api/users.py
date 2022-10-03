from fastapi import APIRouter, HTTPException

import schemas.user
from services.user import user_service

router = APIRouter()

@router.post("/", reponse_model=schemas.User)
def create_user(obj : schemas.user.UserCreate):
    user = user_service.get_user_by_username(username = obj.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="이 유저 네임은 이미 존재합니다"
        )
    user = service.create(user_obj = obj)
    return user

