from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from config.database import Base

class Movie_direction(Base):
    __tablename__ = 'movie_direction'

    movie_id = Column(Integer, ForeignKey('movie.id'))
    dir_id = Column(Integer, ForeignKey('direction.id'))
