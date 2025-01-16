from typing import Any

from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer


class SnippetViewSet(viewsets.ModelViewSet[Snippet]):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Snippet._default_manager.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        snippet = self.get_object()
        print(f"id = {snippet.id}")
        print(f"pk = {snippet.pk}")
        print(f"foo_id = {snippet.foo_id}")
        if snippet.foo is not None:
            print(f"foo.id = {snippet.foo.id}")
            print(f"foo.pk = {snippet.foo.pk}")
            print(f"foo.value = {snippet.foo.value}")
        if hasattr(snippet, "bar") and snippet.bar is not None:
            # print(f"bar.id = {snippet.bar.id}")  # Error: "Bar" has no attribute "id"  # noqa: ERA001
            print(f"bar.pk = {snippet.bar.pk}")
            print(f"bar.value = {snippet.bar.value}")
        for baz in snippet.bazs.all():
            print(f"baz.id = {baz.id}")
            print(f"baz.pk = {baz.pk}")
            print(f"baz.value = {baz.value}")
        return Response(snippet.highlighted)

    def perform_create(self, serializer: BaseSerializer[Snippet]) -> None:
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet[User]):
    """This viewset automatically provides `list` and `retrieve` actions."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
