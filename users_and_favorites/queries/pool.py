import os
from psycopg_pool import ConnectionPool

pool = ConnectionPool(conninfo=os.environ["USERS_DATABASE_URL"])
