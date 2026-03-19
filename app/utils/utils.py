import random
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