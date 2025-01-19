from typing import Any

from django.http import HttpRequest
from ninja import Router, Schema

router = Router()


class UserSchema(Schema):
    username: str
    email: str
    first_name: str
    last_name: str


class Error(Schema):
    message: str


@router.get("", response={200: UserSchema, 403: Error})
def me(request: HttpRequest) -> Any:
    if not request.user.is_authenticated:
        return 403, {"message": "Please sign in first"}
    return request.user
