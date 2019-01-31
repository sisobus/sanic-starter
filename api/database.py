""" This module exports the database engine.
Notes:
     Using the scoped_session contextmanager is
     best practice to ensure the session gets closed
     and reduces noise in code by not having to manually
     commit or rollback the db if a exception occurs.
"""
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.config import BaseConfig
from aredis import StrictRedis

engine = create_engine(BaseConfig.SQLALCHEMY_DATABASE_URI)

# Session to be used throughout app.
Session = sessionmaker(bind=engine)
RedisSession = StrictRedis(
    host=BaseConfig.DB_SERVICE, port=BaseConfig.REDIS_PORT, db=0)


@contextmanager
def scoped_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise
    finally:
        session.close()
