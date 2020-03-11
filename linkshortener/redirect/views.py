from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
import redis
from rest_framework import status

redis_db = redis.StrictRedis(decode_responses=True)


class Redirect(View):
    def get(self, request, url_hash):
        url = redis_db.get(url_hash)
        if url:
            redis_db.incr(f"{url_hash}:visits")
            if request.user_agent.is_mobile or request.user_agent.is_tablet:
                redis_db.incr(f"{url_hash}:mobile")
            if request.user_agent.is_pc:
                redis_db.incr(f"{url_hash}:desktop")
            return redirect(url)
        else:
            return HttpResponse("The page was not founded", status=status.HTTP_404_NOT_FOUND)
