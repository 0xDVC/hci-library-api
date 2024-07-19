from dotenv import load_dotenv
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

env_path = Path('../..') / '.env'

DB_URI = 'postgresql://${PG_USER}:${PG_PASSWORD}@${PG_HOST}:${PG_PORT}/${PG_DB}'

engine = create_engine(DB_URI)

Base = declarative_base()

def get_db():
    db = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    try:
        yield db
    finally:
        db.close()


