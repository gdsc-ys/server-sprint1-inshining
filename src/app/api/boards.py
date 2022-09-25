from fastapi import APIRouter, Depends, HTTPException


router = APIRouter()

@router.get("/")
def get_boards():
    return "Hello"
