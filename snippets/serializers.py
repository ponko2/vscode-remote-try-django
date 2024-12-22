from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer[Snippet]):
    class Meta:
        model = Snippet
        fields = ["id", "title", "code", "linenos", "language", "style"]


class UserSerializer(serializers.ModelSerializer[User]):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet._default_manager.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "snippets"]
