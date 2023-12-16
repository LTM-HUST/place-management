from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/place_management"

engine = create_engine(SQLALCHEMY_DATABASE_URL,
    echo=True
)

meta = MetaData()

conn = engine.connect()

Base = declarative_base()