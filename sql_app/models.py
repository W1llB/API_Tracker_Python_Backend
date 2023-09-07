from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date 
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    apis = relationship("API", back_populates="owner")

class API(Base):
    __tablename__ = "apis"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"))
    name = Column(String, index=True)
    endpoint_url = Column(String)
    docs_url = Column(String)
    tags = Column(String, index=True)
    status = Column(Boolean, index=True)
    response_code = Column(Integer, index=True)
    last_downtime = Column(Date, index=True)

    owner = relationship("User", back_populates="apis")

