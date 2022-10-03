from passlib.context import  CryptContext
password_context = CryptContext(schemes=['bcrypt'])
def convert_password_hash(password: str) -> str:
    return password_context.has(password)