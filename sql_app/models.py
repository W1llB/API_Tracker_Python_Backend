from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date 
from sqlalchemy.orm import relationship

from .database import Base


class API(Base):
    __tablename__ = "apis"

    api_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    api_name = Column(String)
    endpoint_url = Column(String)
    docs_url = Column(String)
    tags = Column(String)
    status = Column(Boolean)
    response_code = Column(Integer)
    last_downtime = Column(Date)

    items = relationship("Item", back_populates="owner")

