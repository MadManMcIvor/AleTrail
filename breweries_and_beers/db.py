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
                    SELECT b.beer_id, b.name, b.description, b.type,
                    b.ibu, b.abv, b.website, b.brewery, b.image_url
                    FROM beers.b
                    ORDER BY b.name
                    """
                )
                results = []
                for row in cur.fetchall():
                    record = {}
                    for i, column in enumerate(cur.description):
                        record[column.name] = row[i]
                    results.append(record)

                return results

    def get_beer(self, id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id
                    , name
                    , description
                    , type
                    , ibu
                    , abv
                    , website
                    , brewery
                    , image_url
                    WHERE id = %s
                    """,
                    [id],
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
                    image_url
                    )
                    VALUES (%s
                    , %s
                    , %s
                    , %s
                    , %s
                    , %s
                    , %s)
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
                    ],
                )

                record = None
                row = cur.fetchone()
                if row is not None:
                    record = {}
                    for i, column in enumerate(cur.description):
                        record[column.name] = row[i]
                response = {
                    "id": record["beer_id"],
                    "name": beer.name,
                    "description": beer.description,
                    "type": beer.type,
                    "ibu": beer.ibu,
                    "abv": beer.abv,
                    "website": beer.website,
                    "brewery": beer.brewery,
                    "image_url": beer.image_url,
                }
                return response