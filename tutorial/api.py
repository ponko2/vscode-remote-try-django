from ninja import NinjaAPI

api = NinjaAPI(version="2.0.0")

api.add_router("/hello", "hello.api.router")
