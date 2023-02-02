from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base

class Genres(Base):
    __tablename__ = 'genres'
    gen_id = Column(Integer, primary_key=True, Index=True)
    title = Column(String)
    
