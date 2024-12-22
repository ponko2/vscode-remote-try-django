from typing import Any

from rest_framework import generics, mixins
from rest_framework.request import Request
from rest_framework.response import Response

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView[Snippet],
):
    queryset = Snippet._default_manager.all()
    serializer_class = SnippetSerializer

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.create(request, *args, **kwargs)


class SnippetDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView[Snippet],
):
    queryset = Snippet._default_manager.all()
    serializer_class = SnippetSerializer

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.destroy(request, *args, **kwargs)
