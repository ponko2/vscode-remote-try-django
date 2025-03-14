from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer[Snippet]):
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight",
        format="html",
    )

    class Meta:
        model = Snippet
        fields = [
            "url",
            "id",
            "highlight",
            "owner",
            "title",
            "code",
            "linenos",
            "language",
            "style",
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer[User]):
    snippets = serializers.HyperlinkedRelatedField[Snippet](
        many=True,
        view_name="snippet-detail",
        read_only=True,
    )

    class Meta:
        model = User
        fields = ["url", "id", "username", "snippets"]
