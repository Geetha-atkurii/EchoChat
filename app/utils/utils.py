import random
import re
import string
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserAuthUtils:
    @staticmethod
    def generate_user_id():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    @staticmethod
    def hash_password(password: str):
        return pwd_context.hash(password)
    
    @staticmethod
    def validate_password(password: str):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,16}$"
        if not re.match(pattern, password):
            raise ValueError(
                "Password must be atleast 8-16 chars, including atleast one uppercase, lowercase, number, and a special character."
            )
        return True
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)