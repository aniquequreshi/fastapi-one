from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# import os
# from dotenv import load_dotenv
# load_dotenv()
# junk = os.getenv('DB_URL')
# print(junk)

SQLALCHEMY_DATABASE_URL = "db connection string"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
