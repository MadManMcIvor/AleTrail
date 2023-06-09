from pydantic import BaseModel
from db import pool
from typing import List, Optional
from pprint import pprint


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
    beer_favorite_id: int
    user_id: int
    beer_id: int
    name: str
    description: str
    type: str
    ibu: int
    abv: float
    brewery: int
    image_url: str
    category: str
    vegetarian_friendly: bool


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
                        [user_id],
                    )
                    temp_list = [item for item in result]
                    pprint(temp_list)
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
                            website=record[11],
                        )
                        for record in temp_list
                    ]
        except Exception:
            return {"message:" "Could not get all brewery favorites"}

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
                    [brewery_favorite.user_id, brewery_favorite.brewery_id],
                )
                row = result.fetchone()
                brewery_favorite_id = row[0]
                old_data = brewery_favorite.dict()
                return BreweryFavoriteOut(
                    brewery_favorite_id=brewery_favorite_id, **old_data
                )

    def delete(self, brewery_favorite_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM brewery_favorites
                        WHERE brewery_favorite_id = %s
                        """,
                        [brewery_favorite_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False


class BeerFavoritesRepository:
    def get_all(self, user_id) -> List[BeerFavoriteJoinOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    result = cur.execute(
                        """
                        SELECT fav.beer_favorite_id, 
                            fav.user_id, 
                            fav.beer_id, 
                            brew.name, 
                            brew.description, 
                            brew.type,
                            brew.ibu,
                            brew.abv,
                            brew.brewery,
                            brew.image_url,
                            brew.category,
                            brew.vegetarian_friendly 
                        FROM beer_favorites AS fav
                        INNER JOIN beers AS brew
                        ON (fav.beer_id = brew.beer_id)
                        WHERE fav.user_id = %s;
                        """,
                        [user_id],
                    )
                    temp_list = [item for item in result]
                    print(temp_list)
                    return [
                        BeerFavoriteJoinOut(
                            beer_favorite_id=record[0],
                            user_id=record[1],
                            beer_id=record[2],
                            name=record[3],
                            description=record[4],
                            type=record[5],
                            ibu=record[6],
                            abv=record[7],
                            brewery=record[8],
                            image_url=record[9],
                            category=record[10],
                            vegetarian_friendly=record[11],
                        )
                        for record in temp_list
                    ]
        except Exception:
            return {"message:" "Could not get all brewery favorites"}

    def create(self, beer_favorite: BeerFavoriteIn) -> BeerFavoriteOut:
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
                    [beer_favorite.user_id, beer_favorite.beer_id],
                )
                row = result.fetchone()
                beer_favorite_id = row[0]
                old_data = beer_favorite.dict()
                return BeerFavoriteOut(beer_favorite_id=beer_favorite_id, **old_data)

    def delete(self, beer_favorite_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM beer_favorites
                        WHERE beer_favorite_id = %s
                        """,
                        [beer_favorite_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False
