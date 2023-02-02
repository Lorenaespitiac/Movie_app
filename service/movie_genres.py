from models.movie_genres import MoviesGenres as MoviesGenresModel
from schemas.movie_genres import MoviesGenres


class MoviesGenresService():
    
    def __init__(self,db) -> None:
        self.db = db
        
    def get_movies_genres(self):
        result = self.db.query(MoviesGenresModel).all()
        return result
    
    def get_movies_genres(self,movie_id:int):
    
        result = self.db.query(MoviesGenresModel).filter(MoviesGenresModel.movie_id == movie_id).first()
        return result
    
    def get_movies_genres_by_gen_id(self, gen_id:int):
        result= self.db.query(MoviesGenresModel).filter(MoviesGenresModel).all()
        return result
        
    def create_movies_genres(self, movie_genres:MoviesGenres):
        new_movies_genres = MoviesGenresModel(
            movie_id= movie_genres.movie_id,
           gen_id= movie_genres.gen_id
        )
        
        self.db.add(new_movies_genres)
        self.db.commit()
        return

    def update_movies_genres(self, movie_id:int, data:MoviesGenres):
        movies_genres = self.db.query(MoviesGenresModel).filter(MoviesGenresModel.movie_id == movie_id).first()
        movies_genres.gen_id = data.gen_id
        self.db.commit()
        return
        
    def delete_movies_genres(self, movie_id:int):
        self.db.query(MoviesGenresModel).filter(MoviesGenresModel.movie_id==movie_id).delete()
        self.db.commit()
        return