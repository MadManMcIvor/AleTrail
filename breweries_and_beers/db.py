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

    # def create_brewery(self, brewery):
    #     id = None
    #     with pool.connection() as conn:
    #         with conn.cursor() as cur:
    #             cur.execute(
    #                 """
    #                 INSERT INTO breweries (
    #                     name, street, city, state, zip_code, phone, image_url, description, website
    #                 )
    #                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,)
    #                 RETURNING id
    #                 """,
    #                 [
    #                     brewery.name,
    #                     brewery.street,
    #                     brewery.city,
    #                     brewery.state,
    #                     brewery.zip_code,
    #                     brewery.phone,
    #                     brewery.image_url,
    #                     brewery.description,
    #                     brewery.website,
    #                 ],
    #             )
    #             row = cur.fetchone()
    #             id = row[0]
    #             if id is not None:
    #                 return self.get_breweries()

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
