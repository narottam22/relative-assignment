#!/usr/bin/env python

from sqlalchemy import Integer, Column
from database import Base

class goerli(Base):
    __tablename__ = "goerli"

    id = Column(Integer, primary_key=True)
    lotcreated = Column(Integer)
    lotjoined = Column(Integer)
    lotresolved = Column(Integer)