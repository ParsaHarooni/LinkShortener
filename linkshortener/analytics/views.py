import redis
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

redis_db = redis.StrictRedis()


class GetAllVisits(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = request.GET
        url_hash = data.get("hash")
        if url_hash:
            all = redis_db.get(f"{url_hash}:visits")
            mobile = redis_db.get(f"{url_hash}:mobile")
            desktop = redis_db.get(f"{url_hash}:desktop")
            return Response(dict(all=all, mobile=mobile, desktop=desktop))
