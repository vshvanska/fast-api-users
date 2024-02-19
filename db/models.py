import datetime

from sqlalchemy import Integer, String, DateTime, func, Column
from sqlalchemy.orm import Mapped, mapped_column
from db.engine import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    register_date = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.username!r})"
