from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import Mapped, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Contacts(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    birthday = Column(Date)

