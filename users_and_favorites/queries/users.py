from turtle import st
from pydantic import BaseModel
from typing import Optional, Union
from queries.pool import pool


class DuplicateAccountError(ValueError):
    pass


class Error(BaseModel):
    message: str


class UserIn(BaseModel):
    first: str
    last: str
    profile_pic: Optional[str]
    email: str
    username: str
    password: str
    is_brewery_owner: bool


class UserOut(BaseModel):
    id: int
    first: str
    last: str
    profile_pic: Optional[str]
    email: str
    username: str
    is_brewery_owner: bool  

class UserOutWithPassword(UserOut):
    hashed_password: str

class UsersOut(BaseModel):
    users: list[UserOut]


class AccountIn(BaseModel):
    email: str 
    password: str 

class AccountOut(BaseModel):
    email: str 

class UserQueries:
    def get(self, email) -> UserOutWithPassword:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                        SELECT *
                        FROM users
                        WHERE email = %s 
                    """,
                        [email],
                    )
    
                for row in cur.fetchall():
                    record = {}
                    for i, column in enumerate(cur.description):
                        record[column.name] = row[i]              
                return record 

    # list all users for admin 
    def get_all_users(self):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, first, last, profile_pic,
                        email, profile_pic, username, is_brewery_owner  
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

    # get user detail 
    def get_user(self, id) -> Optional[UserOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT id, first, last, profile_pic,
                            email, username, is_brewery_owner 
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
                    if record is None:
                        return None
                    return record
        except Exception as e:
            print(e)
            return {"message": "Could not get that user"}

    # def create_user(self, user: UserIn) -> Union[UserOut, Error]:
    #     try:
    #         with pool.connection() as conn:
    #             with conn.cursor() as cur:
    #                 params = [
    #                     user.first,
    #                     user.last,
    #                     user.profile_pic,
    #                     user.email,
    #                     user.username,
    #                     user.password,
    #                     user.is_brewery_owner,
    #                 ]
    #                 cur.execute(
    #                     """
    #                     INSERT INTO users (first, last, profile_pic, email, username, password, is_brewery_owner)
    #                     VALUES (%s, %s, %s, %s, %s, %s, %s)
    #                     RETURNING id, first, last, profile_pic, email, username, is_brewery_owner 
    #                     """,
    #                     params,
    #                 )
    #                 record = None
    #                 row = cur.fetchone()
    #                 if row is not None:
    #                     record = {}
    #                     for i, column in enumerate(cur.description):
    #                         record[column.name] = row[i]
    #                 return record
    #     except Exception:
    #         return {"message": "Can't create user"}

    def create_account(self, info: UserIn, hashed_password: str) -> UserOutWithPassword:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                params = [
                    info.first,
                    info.last,
                    info.profile_pic,
                    info.email,
                    info.username,
                    hashed_password,
                    info.is_brewery_owner,
                ]
                cur.execute(
                    """
                    INSERT INTO users (first, last, profile_pic, email, username, password, is_brewery_owner)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    RETURNING id, first, last, profile_pic, email, username, password, is_brewery_owner 
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


    def update_user(self, user_id: int, user: UserIn, hashed_password: str) -> UserOutWithPassword:
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
                        , password = %s
                        , is_brewery_owner = %s
                        WHERE id = %s
                        RETURNING id, first, last, profile_pic, email, username, password, is_brewery_owner
                        """,
                        [
                            user.first,
                            user.last,
                            user.profile_pic,
                            user.email,
                            user.username,
                            hashed_password,
                            user.is_brewery_owner, 
                            user_id,
                        ],
                    )
                    # old_data = user.dict()
                    # return UserOut(id=user_id, **old_data)
                    record = None
                    row = cur.fetchone()
                    if row is not None:
                        record = {}
                        for i, column in enumerate(cur.description):
                            record[column.name] = row[i]
                    return record
        except Exception as e:
            print(e)
            return {"message": "Could not update user"}

    def delete_user(self, user_id: int) -> bool:
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
