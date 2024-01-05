from database import Base,engine
from models import User, Place, Friend, Tag, Category

Base.metadata.create_all(engine)