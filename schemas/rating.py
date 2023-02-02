from pydantic import BaseModel


class Rating(BaseModel):
    movie_id: int
    rev_id: int
    rev_stars: int
    num_o_rating: int
    
    class Config:
        schema_extra= {
            "example": {
                'movie_id': 2,
                'rev_id': 3,
                'rev_stars': 4,
                'num_o_rating': 1,
            }
        }
        