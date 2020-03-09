from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import USER_MODEL, UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = USER_MODEL.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
