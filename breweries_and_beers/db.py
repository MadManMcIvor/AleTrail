import os
from psycopg_pool import ConnectionPool

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])

class BreweryQueries:
    def get_breweries(self):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT brew.brewery_id, brew.name, brew.street,
                        brew.city, brew.state, brew.zip_code,
                        brew.phone, brew.image_url, brew.description,
                        brew.website
                    FROM breweries brew
                    ORDER BY brew.name
                    """
                )
                breweries = []
                rows = cur.fetchall()
                for row in rows:
                    brewery = self.brewery_record_to_dict(row, cur.description)
                    breweries.append(brewery)
                return breweries

    def get_breweries_by_city(self, city):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT *
                    FROM breweries brew
                    WHERE brew.city = %s
                    """,
                    [city]
                )

                breweries = []
                rows = cur.fetchall()
                for row in rows:
                    brewery = self.brewery_record_to_dict(row, cur.description)
                    breweries.append(brewery)
                print(breweries)
                return breweries
    

    def get_brewery(self, brewery_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT brew.brewery_id, brew.name, brew.street,
                        brew.city, brew.state, brew.zip_code,
                        brew.phone, brew.image_url, brew.description,
                        brew.website
                    FROM breweries brew
                    WHERE brew.brewery_id = %s
                    """,
                    [brewery_id],
                )

                row = cur.fetchone()
                return self.brewery_record_to_dict(row, cur.description)

    def create_brewery(self, brewery):
        brewery_id = None
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO breweries (
                        name, street, city, state, zip_code, phone, image_url, description, website
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING brewery_id
                    """,
                    [
                        brewery.name,
                        brewery.street,
                        brewery.city,
                        brewery.state,
                        brewery.zip_code,
                        brewery.phone,
                        brewery.image_url,
                        brewery.description,
                        brewery.website,
                    ],
                )
                row = cur.fetchone()
                brewery_id = row[0]
        if brewery_id is not None:
            return self.get_brewery(brewery_id)

    def delete_brewery(self, brewery_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    DELETE FROM breweries
                    WHERE brewery_id = %s
                    """,
                    [brewery_id],
                )

    def update_brewery(self, brewery_id, brewery):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                params = [
                    brewery.name,
                    brewery.street,
                    brewery.city,
                    brewery.state,
                    brewery.zip_code,
                    brewery.phone,
                    brewery.image_url,
                    brewery.description,
                    brewery.website,
                    brewery_id
                ]
                cur.execute(
                    """
                    UPDATE breweries
                    SET name = %s
                        , street = %s
                        , city = %s
                        , state = %s
                        , zip_code = %s
                        , phone = %s
                        , image_url = %s
                        , description = %s
                        , website = %s
                    WHERE brewery_id = %s
                    RETURNING brewery_id, name, street, city, state, zip_code, phone, image_url, description, website
                    """,
                    params,
                )

                record = None
                row = cur.fetchone()
                if row is not None:
                    record = {}
                    for i, column in enumerate(cur.description):
                        record[column.name] = row[i]
                return record

    def brewery_record_to_dict(self, row, description):
        brewery = None
        if row is not None:
            brewery = {}
            brewery_fields = [
                "brewery_id",
                "name",
                "street",
                "city",
                "state",
                "zip_code",
                "phone",
                "image_url",
                "description",
                "website",
            ]
            for i, column in enumerate(description):
                if column.name in brewery_fields:
                    brewery[column.name] = row[i]
            brewery["id"] = brewery["brewery_id"]
        return brewery


class BeerQueries:
    def get_beers(self):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT beer_id,
                    name,
                    description,
                    type,
                    ibu,
                    abv,
                    brewery,
                    image_url,
                    category,
                    vegetarian_friendly
                    FROM beers beer
                    ORDER BY name
                    """
                )
                results = []
                for row in cur.fetchall():
                    record = {}
                    for i, column in enumerate(cur.description):
                        record[column.name] = row[i]
                    results.append(record)

                return results

    def get_beer(self, beer_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT beer_id,
                    name,
                    description,
                    type,
                    ibu,
                    abv,
                    brewery,
                    image_url,
                    category,
                    vegetarian_friendly
                    FROM beers beer
                    WHERE beer_id = %s
                    """,
                    [beer_id],
                )

                record = None
                row = cur.fetchone()
                if row is not None:
                    record = {}
                    for i, column in enumerate(cur.description):
                        record[column.name] = row[i]

                return record

    def create_beer(self, beer):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO beers (
                    name,
                    description,
                    type,
                    ibu,
                    abv,
                    brewery,
                    image_url,
                    category,
                    vegetarian_friendly
                    )
                    VALUES (%s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s)
                    RETURNING beer_id
                    """,
                    [
                        beer.name,
                        beer.description,
                        beer.type,
                        beer.ibu,
                        beer.abv,
                        beer.brewery,
                        beer.image_url,
                        beer.category,
                        beer.vegetarian_friendly,
                    ],
                )

                record = None
                row = cur.fetchone()
                if row is not None:
                    record = {}
                    for i, column in enumerate(cur.description):
                        record[column.name] = row[i]
                response = {
                    "beer_id": record["beer_id"],
                    "name": beer.name,
                    "description": beer.description,
                    "type": beer.type,
                    "ibu": beer.ibu,
                    "abv": beer.abv,
                    "brewery": beer.brewery,
                    "image_url": beer.image_url,
                    "category" : beer.category,
                    "vegetarian_friendly" : beer.vegetarian_friendly,
                }
                return response

    def update_beer(self, beer_id, beer):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                params = [
                    beer.name,
                    beer.description,
                    beer.type,
                    beer.ibu,
                    beer.abv,
                    beer.brewery,
                    beer.image_url,
                    beer.category,
                    beer.vegetarian_friendly,
                    beer_id
                ]
                cur.execute(
                    """
                    UPDATE beers
                    SET name = %s
                    , description = %s
                    , type = %s
                    , ibu = %s
                    , abv = %s
                    , brewery = %s
                    , image_url = %s
                    , category = %s
                    , vegetarian_friendly = %s
                    WHERE beer_id = %s
                    RETURNING beer_id, name, description, type, ibu, abv, brewery, image_url, category, vegetarian_friendly
                    """,
                    params,
                )

                record = None
                row = cur.fetchone()
                if row is not None:
                    record = {}
                    for i, column in enumerate(cur.description):
                        record[column.name] = row[i]
                return record

    def delete_beer(self, beer_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    DELETE FROM beers
                    WHERE beer_id = %s
                    """,
                    [beer_id],
                )