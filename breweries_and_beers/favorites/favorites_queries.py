from pydantic import BaseModel
from breweries_and_beers.db import pool
from typing import List, Optional

class BreweryFavoriteIn(BaseModel):
    user_id: int
    brewery_id: int

class BreweryFavoriteOut(BaseModel):
    brewery_favorite_id: int
    user_id: int
    brewery_id: int

class BreweryFavoriteJoin(BaseModel):
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
    beers: Optional[str]


class BeerFavoriteIn(BaseModel):
    user_id: int
    beer_id: int

class BeerFavoriteOut(BaseModel):
    beer_favorite_id: int
    user_id: int
    beer_id: int


class BreweryFavoritesRepository:
    def get_all(self, user_id) -> List[BreweryFavoriteOut]:
        try:
            print("LOOOOOOK HERE!!! USER ID:", user_id)
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    result = cur.execute(
                        """
                        SELECT * 
                        FROM brewery_favorites as fav
                        WHERE fav.user_id = %s; 
                        """,
                        [user_id]
                    )
                    print("LOOOOOOK HERE!!! CUR:", cur)
                    return [
                        BreweryFavoriteOut(
                            brewery_favorite_id=record[0],
                            user_id=record[1],
                            brewery_id=record[2],
                        ) for record in cur
                    ]
        except Exception:
            return {'message:' 'Could not get all brewery favorites'}


    def create(self, brewery_favorite: BreweryFavoriteIn) -> BreweryFavoriteOut:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                result = cur.execute(
                    """
                    INSERT INTO brewery_favorites
                        (user_id, brewery_id)
                    VALUES
                        (%s, %s)
                    RETURNING brewery_favorite_id;
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


#   SELECT fav.brewery_favorite_id, brew.brewery_id, brew.name, brew.street,
#                         brew.city, brew.state, brew.zip_code,
#                         brew.phone, brew.image_url, brew.description,
#                         brew.website
#                         FROM users_and_favorites.brewery_favorites AS f
#                         INNER JOIN breweries_and_beers.breweries AS brew
#                             ON (fav.brewery_id = brew.brewery_id)