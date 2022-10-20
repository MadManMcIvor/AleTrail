from pydantic import BaseModel
from db import pool
from typing import List, Optional

class BreweryFavoriteIn(BaseModel):
    user_id: int
    brewery_id: int

class BreweryFavoriteOut(BaseModel):
    brewery_favorite_id: int
    user_id: int
    brewery_id: int

class BreweryFavoriteJoinOut(BaseModel):
    brewery_favorite_id: int
    user_id: int
    brewery_id: int
    name: str
    street: str
    city: str
    state: str
    zip_code: int
    phone: Optional[str]
    image_url: Optional[str]
    description: Optional[str]
    website: Optional[str]

class BeerFavoriteIn(BaseModel):
    user_id: int
    beer_id: int

class BeerFavoriteOut(BaseModel):
    beer_favorite_id: int
    user_id: int
    beer_id: int

class BeerFavoriteJoinOut(BaseModel):
    brewery_favorite_id: int
    user_id: int
    brewery_id: int
    name: str
    street: str
    city: str
    state: str
    zip_code: int
    phone: Optional[str]
    image_url: Optional[str]
    description: Optional[str]
    website: Optional[str]


class BreweryFavoritesRepository:
    def get_all(self, user_id) -> List[BreweryFavoriteJoinOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    result = cur.execute(
                        """
                        SELECT fav.brewery_favorite_id, 
                            fav.user_id, 
                            fav.brewery_id, 
                            brew.name,
                            brew.street, 
                            brew.city, 
                            brew.state, 
                            brew.zip_code, 
                            brew.phone, 
                            brew.image_url, 
                            brew.description, 
                            brew.website 
                        FROM brewery_favorites AS fav
                        INNER JOIN breweries AS brew
                        ON (fav.brewery_id = brew.brewery_id)
                        WHERE fav.user_id = %s;
                        """,
                        [user_id]
                    )
                    temp_list = [item for item in result]
                    return [
                        BreweryFavoriteJoinOut(
                            brewery_favorite_id=record[0],
                            user_id=record[1],
                            brewery_id=record[2],
                            name=record[3],
                            street=record[4],
                            city=record[5],
                            state=record[6],
                            zip_code=record[7],
                            phone=record[8],
                            image_url=record[9],
                            description=record[10],
                            website=record[11]
                        ) for record in temp_list
                    ]
        except Exception:
            return {'message:' 'Could not get all brewery favorites'}


    def create(self, brewery_favorite: BreweryFavoriteIn) -> BreweryFavoriteOut:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                result = cur.execute(
                    """
                    INSERT INTO beer_favorites
                        (user_id, beer_id)
                    VALUES
                        (%s, %s)
                    RETURNING beer_favorite_id;
                    """,
                    [
                        brewery_favorite.user_id, 
                        brewery_favorite.brewery_id
                    ]
                )
                row = result.fetchone()
                brewery_favorite_id = row[0]
                old_data = brewery_favorite.dict()
                return BreweryFavoriteOut(brewery_favorite_id=brewery_favorite_id, **old_data)
    


class BeerFavoritesRepository:
    def get_all(self, user_id) -> List[BeerFavoriteJoinOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    result = cur.execute(
                        """
                        SELECT fav.brewery_favorite_id, 
                            fav.user_id, 
                            fav.brewery_id, 
                            brew.name,
                            brew.street, 
                            brew.city, 
                            brew.state, 
                            brew.zip_code, 
                            brew.phone, 
                            brew.image_url, 
                            brew.description, 
                            brew.website 
                        FROM brewery_favorites AS fav
                        INNER JOIN breweries AS brew
                        ON (fav.brewery_id = brew.brewery_id)
                        WHERE fav.user_id = %s;
                        """,
                        [user_id]
                    )
                    temp_list = [item for item in result]
                    return [
                        BeerFavoriteJoinOut(
                            brewery_favorite_id=record[0],
                            user_id=record[1],
                            brewery_id=record[2],
                            name=record[3],
                            street=record[4],
                            city=record[5],
                            state=record[6],
                            zip_code=record[7],
                            phone=record[8],
                            image_url=record[9],
                            description=record[10],
                            website=record[11]
                        ) for record in temp_list
                    ]
        except Exception:
            return {'message:' 'Could not get all brewery favorites'}


    def create(self, brewery_favorite: BeerFavoriteIn) -> BeerFavoriteOut:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                result = cur.execute(
                    """
                    INSERT INTO beer_favorites
                        (user_id, beer_id)
                    VALUES
                        (%s, %s)
                    RETURNING beer_favorite_id;
                    """,
                    [
                        beer_favorite.user_id, 
                        beer_favorite.beer_id
                    ]
                )
                row = result.fetchone()
                beer_favorite_id = row[0]
                old_data = brewery_favorite.dict()
                return BeerFavoriteOut(beer_favorite_id=beer_favorite_id, **old_data)
    
