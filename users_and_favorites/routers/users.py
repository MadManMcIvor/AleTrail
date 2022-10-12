from urllib import response
from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)

from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from pydantic import BaseModel
from typing import Union, Optional
from queries.users import (
    Error,
    UserIn,
    UserOut,
    UsersOut,
    UserQueries,
    DuplicateAccountError,
)

class AccountForm(BaseModel):
    username: str
    password: str


class AccountToken(Token):
    user: UserOut


class HttpError(BaseModel):
    detail: str


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


@router.get("/protected", response_model=bool)
async def get_protected(
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    return True


# @router.get("/api/vacations", response_model = bool)
# async def get_protected(
#     vacations: VacationQueries = Depends(),
#     account_data: dict = Depends(authenticator.get_current_account_data),
# ):
#     return vacations.get_account_vacations(account_data)


@router.get("/token", response_model=AccountToken | None)
async def get_token(
    request: Request,
    user: UserOut = Depends(authenticator.try_get_current_account_data),
) -> AccountToken | None:
    if authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "user": user,
        }


# @router.post("/users", response_model=Union[UserOut, Error])
# def create_user(
#     user_in: UserIn,
#     queries: UserQueries = Depends(),
# ) -> Union[UserOut, Error]:
#     return queries.create_user(user_in)


@router.post("/users", response_model=AccountToken | HttpError)
async def create_account(
    info: UserIn,
    request: Request,
    response: Response,
    users: UserQueries = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)
    try:
        user = users.create_account(info, hashed_password)
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    form = AccountForm(username=info.email, password= info.password)
    token = await authenticator.login(response, request, form, users)
    return AccountToken(user=user, **token.dict())



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
