from typing import Any

from django.db import models
from django_stubs_ext.db.models import TypedModelMeta
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Foo(models.Model):
    value = models.TextField()

    class Meta(TypedModelMeta):
        ordering = ["value"]


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default="python", max_length=100
    )
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100)
    owner = models.ForeignKey(
        "auth.User", related_name="snippets", on_delete=models.CASCADE
    )
    highlighted = models.TextField()
    foo = models.ForeignKey(
        Foo,
        null=True,
        on_delete=models.SET_NULL,
        related_name="snippets",
    )

    class Meta(TypedModelMeta):
        ordering = ["created"]

    def save(self, *args: Any, **kwargs: Any) -> None:
        """Use the `pygments` library to create a highlighted HTML representation of the code snippet."""
        lexer = get_lexer_by_name(self.language)
        linenos = "table" if self.linenos else False
        options = {"title": self.title} if self.title else {}
        formatter = HtmlFormatter(
            style=self.style,
            linenos=linenos,
            full=True,
            encoding=None,
            outencoding=None,
            **options,
        )
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)


class Bar(models.Model):
    value = models.TextField()
    snippet = models.OneToOneField(
        Snippet,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="bar",
    )

    class Meta(TypedModelMeta):
        ordering = ["value"]


class Baz(models.Model):
    value = models.TextField()
    snippet = models.ForeignKey(
        Snippet,
        null=True,
        on_delete=models.SET_NULL,
        related_name="bazs",
    )

    class Meta(TypedModelMeta):
        ordering = ["value"]
