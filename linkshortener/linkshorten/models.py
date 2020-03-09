from django.contrib.auth import get_user_model
from django.db import models
import base62

USER_MODEL = get_user_model()


class Link(models.Model):
    url = models.URLField()
    hash = models.CharField(max_length=2048, unique=True, null=True)
    owner = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    @classmethod
    def shorten_link(cls, url, user, url_hash=None):
        shortened_link = cls(url=url, owner=user, hash=url_hash)
        shortened_link.save()
        if url_hash is None:
            shortened_link.hash = base62.encode(shortened_link.pk)
        shortened_link.save()
        return shortened_link
