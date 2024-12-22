from django.contrib.auth.models import User
from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer


class SnippetList(generics.ListCreateAPIView[Snippet]):
    queryset = Snippet._default_manager.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView[Snippet]):
    queryset = Snippet._default_manager.all()
    serializer_class = SnippetSerializer


class UserList(generics.ListAPIView[User]):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView[User]):
    queryset = User.objects.all()
    serializer_class = UserSerializer
