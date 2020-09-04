from sqlalchemy import Column, String, Text, ForeignKey, func, text
from sqlalchemy.dialects.mysql import BIGINT, TIMESTAMP

from .base import Base


class Notes(Base):
    __tablename__ = 'notes'

    id = Column(BIGINT(unsigned=True), primary_key=True)
    user_id = Column(BIGINT(unsigned=True),
                     ForeignKey('users.id'))
    title = Column(String(255), nullable=True,
                   index=True, unique=False)
    body = Column(Text, nullable=False,
                  index=False, unique=False)

    created_at = Column(TIMESTAMP,
                        server_default=func.now(),
                        unique=False,
                        nullable=False,
                        index=True
                        )
    updated_at = Column(TIMESTAMP,
                        nullable=False,
                        index=True,
                        unique=False,
                        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
                        )
