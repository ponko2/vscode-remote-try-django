from django.http import HttpRequest
from ninja import Router

router = Router()


@router.get("")
def hello(request: HttpRequest, name: str = "world") -> str:
    return f"Hello {name}"
