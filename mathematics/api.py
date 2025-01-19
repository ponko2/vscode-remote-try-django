from django.http import HttpRequest
from ninja import Router

router = Router()


@router.get("/{a}and{b}")
def math(request: HttpRequest, a: int, b: int) -> dict[str, int]:
    return {"add": a + b, "multiply": a * b}
