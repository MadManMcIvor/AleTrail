import os
from psycopg_pool import ConnectionPool
from pprint import pprint

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
                        brew.website, beers.beer_id, beers.name AS beers
                    FROM beers
                    RIGHT JOIN breweries brew ON(beers.brewery = brew.brewery_id)
                    GROUP BY brew.brewery_id, brew.name, brew.street,
                        brew.city, brew.state, brew.zip_code,
                        brew.phone, brew.image_url, brew.description,
                        brew.website, beers.beer_id, beers
                    """
                )
                breweries = []
                rows = cur.fetchall()
                for row in rows:
                    brewery = self.brewery_record_to_dict(row, cur.description)
                    breweries.append(brewery)
                self.consolidate_beers(breweries)
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
                "beers",
            ]
            
            for i, column in enumerate(description):
                if column.name in brewery_fields:
                    brewery[column.name] = row[i]
            brewery["id"] = brewery["brewery_id"]

        return brewery

    def consolidate_beers(self, breweries):
        # pprint(breweries)
        # print(len(breweries))
        output = []
        brewery_ids = {}
        for i in range(len(breweries)):
            if breweries[i]["brewery_id"] not in brewery_ids:
                brewery_ids[i] = (breweries[i]["brewery_id"])
                output.append(breweries[i])

        pprint(output)
        # print(brewery_ids)
            # for j in range(i+1,len(breweries)):
            #     if breweries[i]["brewery_id"] == breweries[j]["brewery_id"]:
            #         print(breweries[i]["brewery_id"], breweries[j]["brewery_id"])
