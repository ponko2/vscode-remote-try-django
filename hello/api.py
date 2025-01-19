from django.http import HttpRequest
from ninja import Router

router = Router()


@router.get("")
def hello(request: HttpRequest) -> str:
    return "Hello world"
