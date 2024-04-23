from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,
                primary_key=True,
                autoincrement=True)
    id_user = Column(Integer,
                     unique=True)
    tg_username = Column(String,
                         nullable=True,
                         default=None)
    tg_fullname = Column(String,
                         nullable=True,
                         default=None)
