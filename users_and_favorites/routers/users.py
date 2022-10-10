from fastapi import APIRouter, Depends, Response
from typing import Union, Optional
from queries.users import (
    Error,
    UserIn,
    UserOut,
    UsersOut,
)

from queries.users import UserQueries

router = APIRouter()


@router.get("/users", response_model=UsersOut)
def users_list(queries: UserQueries = Depends()):
    return {
        "users": queries.get_all_users(),
    }


@router.get("/users/{user_id}", response_model=Optional[UserOut])
def get_user(user_id: int, response: Response, queries: UserQueries = Depends()):
    record = queries.get_user(user_id)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.post("/users", response_model=Union[UserOut, Error])
def create_user(
    user_in: UserIn,
    queries: UserQueries = Depends(),
) -> Union[UserOut, Error]:
    return queries.create_user(user_in)


@router.put("/users/{user_id}", response_model=Union[UserOut, Error])
def update_user(
    user_id: int,
    user_in: UserIn,
    response: Response,
    queries: UserQueries = Depends(),
) -> Union[Error, UserOut]:
    # return queries.update_user(user_id, user_in)
    record = queries.update_user(user_id, user_in)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.delete("/users/{user_id}", response_model=bool)
def delete_user(
    user_id: int,
    queries: UserQueries = Depends(),
) -> bool:
    return queries.delete_user(user_id)
