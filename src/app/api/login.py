from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from config import security
from config.settings import get_cursor
from db.sql import select_one_sql
from schemas.token import Token
from services.board import board_service
from psycopg2._psycopg import cursor

from services.user import user_service

router = APIRouter()

@router.post("/", response_model=Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_service.authenticate(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400)
    access_token_expire = timedelta(minutes=11520)
    return {
        "access_token" : security.create_access_token(user[0], expire=access_token_expire),
        "token_type": "bearer"
    }