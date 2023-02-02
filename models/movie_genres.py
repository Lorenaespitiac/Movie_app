from sqlalchemy import Column, ForeignKey ,Integer, String, Float,Date
from sqlalchemy.orm import relationship

from config.database import Base

class MoviesGenres(Base):

    __tablename__="movies_genres"

    movie_id = Column(Integer, ForeignKey('movies.id'))
    gen_id = Column(Integer, ForeignKey('genres.id'))
