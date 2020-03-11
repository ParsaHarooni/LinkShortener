from django.db import IntegrityError
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from linkshorten.models import Link
import redis

redis_db = redis.Redis()


class ShortenLink(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        url = data.get("url")
        if url is None:
            resp = dict(message="Please provide url")
            return Response(status=status.HTTP_400_BAD_REQUEST, data=resp)
        url_hash = data.get("hash")
        try:
            shorten_url = Link.shorten_link(url=url, user=request.user, url_hash=url_hash)
            resp = dict(shorten_url=f"http://localhost:8000/r/{shorten_url.hash}/", hash=shorten_url.hash)
            redis_db.set(shorten_url.hash, url)
            return Response(status=status.HTTP_201_CREATED, data=resp)
        except IntegrityError:
            resp = dict(message="This hash already exists.")
            return Response(status=status.HTTP_400_BAD_REQUEST, data=resp)
