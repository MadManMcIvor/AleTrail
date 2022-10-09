from pydantic import BaseModel
from typing import Optional, Union
from queries.pool import pool 

class Error(BaseModel):
    message: str

class UserIn(BaseModel):
    first: str
    last: str
    profile_pic: Optional[str]
    email: str
    username: str


class UserOut(BaseModel):
    id: int
    first: str
    last: str
    profile_pic: Optional[str]
    email: str
    username: str

class UsersOut(BaseModel):
    users: list[UserOut]

class UserQueries:
    def get_all_users(self):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                """
                    SELECT id, first, last, profile_pic,
                        email, profile_pic, username
                    FROM users
                    ORDER BY last, first
                """
                )

                results = []
                for row in cur.fetchall():
                    record = {}
                    for i, column in enumerate(cur.description):
                        record[column.name] = row[i]
                    results.append(record)

                return results

    def get_user(self, id):
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                    """
                        SELECT id, first, last, profile_pic,
                            email, username
                        FROM users
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
        except Exception as e:
            print(e)
            return {"message": "Could not get that user"}


    def create_user(self, user: UserIn) -> Union[UserOut, Error]:
        try: 
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    params = [
                        user.first,
                        user.last,
                        user.profile_pic,
                        user.email,
                        user.username,
                    ]
                    cur.execute(
                        """
                        INSERT INTO users (first, last, profile_pic, email, username)
                        VALUES (%s, %s, %s, %s, %s)
                        RETURNING id, first, last, profile_pic, email, username
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
        except Exception:
            return {"message": "Can't create user"}


    def update_user(self, user_id: int, user: UserIn) -> Union[UserOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        UPDATE users
                        SET first = %s
                        , last = %s
                        , profile_pic = %s
                        , email = %s
                        , username = %s
                        WHERE id = %s
                        RETURNING id, first, last, profile_pic, email, username
                        """,
                        [
                            user.first,
                            user.last,
                            user.profile_pic,
                            user.email,
                            user.username,
                            user_id,
                        ]
                    )
                    old_data = user.dict()
                    return UserOut(id=user_id, **old_data)
        except Exception as e:
            print(e)
            return {"message": "Could not update user"}


    def delete_user(self, user_id:int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        DELETE FROM users
                        WHERE id = %s
                        """,
                        [user_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False 
    
