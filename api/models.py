# import os
from datetime import datetime
# from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    email = Column(String(300))
    password = Column(String(300))
    created_at = Column(DateTime)
    level = Column(Integer)

    def __init__(self, name, email, password, level=0):
        self.name = name
        self.email = email
        self.created_at = datetime.now()
        self.password = password
        self.level = level

    def to_dict(self):
        return {
            "user_id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at.strftime("%Y-%m-%dT%H:%M:%S"),
            "level": self.level
        }

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


class LoginSession(Base):
    __tablename__ = 'login_session'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    jti = Column(String(500))
    created_at = Column(DateTime)

    def __init__(self, user_id, jti):
        self.user_id = user_id
        self.jti = jti
        self.created_at = datetime.now()
