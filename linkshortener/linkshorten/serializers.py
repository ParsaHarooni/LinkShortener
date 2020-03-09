from rest_framework.serializers import ModelSerializer

from authentication.serializers import UserSerializer
from linkshorten.models import Link


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
