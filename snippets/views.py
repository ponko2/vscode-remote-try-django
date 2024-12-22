from typing import Optional

from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.serializers import BaseSerializer

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer


@api_view(["GET"])
def api_root(request: Request, format: Optional[str] = None) -> Response:
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "snippets": reverse("snippet-list", request=request, format=format),
        }
    )


class SnippetList(generics.ListCreateAPIView[Snippet]):
    queryset = Snippet._default_manager.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer: BaseSerializer[Snippet]) -> None:
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView[Snippet]):
    queryset = Snippet._default_manager.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView[User]):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView[User]):
    queryset = User.objects.all()
    serializer_class = UserSerializer
