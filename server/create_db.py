from database import Base,engine
from models import User, Place, Friend, Tag, Category

print("Creating database ....")

Base.metadata.create_all(engine)