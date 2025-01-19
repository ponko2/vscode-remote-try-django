from ninja import NinjaAPI

api = NinjaAPI(version="2.0.0")

api.add_router("/hello", "hello.api.router")
api.add_router("/math", "mathematics.api.router")
api.add_router("/me", "me.api.router")
