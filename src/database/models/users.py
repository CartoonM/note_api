from sqlalchemy import Column, String, func
from sqlalchemy.dialects.mysql import BIGINT, TIMESTAMP

from .base import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(BIGINT(unsigned=True), primary_key=True)

    username = Column(String(255), nullable=False,
                      index=True, unique=True)
    email = Column(String(255), nullable=False,
                   index=True, unique=True)
    password_hash = Column(String(255), nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now(),
                                   nullable=False, index=True)
