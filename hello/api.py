from django.http import HttpRequest
from ninja import Router, Schema

router = Router()


class HelloSchema(Schema):
    name: str = "world"


@router.post("")
def hello(request: HttpRequest, data: HelloSchema) -> str:
    return f"Hello {data.name}"
