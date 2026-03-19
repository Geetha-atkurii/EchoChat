from app.database.session import engine
from app.database.base import Base
from app.users_module.models.user_model import User

def init_db():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!!")
