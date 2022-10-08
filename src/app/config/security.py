from datetime import timedelta, datetime
from typing import Union, Any
import secrets

from jose import jwt
from passlib.context import  CryptContext

password_context = CryptContext(schemes=['bcrypt'])
def convert_password_hash(password: str) -> str:
    return password_context.hash(password)

def create_access_token(subject : Union[str, Any], expire: timedelta = None):
    if expire:
        expire = datetime.utcnow() + expire
    else:
        expire = datetime.utcnow() + timedelta(
            minutes= 11520
        )
    encode_data = {"expire": expire, "subject": str(subject)}
    encoded_jwt  = jwt.encode(encode_data, secrets.token_urlsafe(32), algorithm="HS256")
    return encoded_jwt

def verify_password(plain_password:str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)