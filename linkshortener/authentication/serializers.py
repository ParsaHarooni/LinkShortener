from django.contrib.auth import get_user_model
from rest_framework import serializers

USER_MODEL = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = USER_MODEL
        fields = ('id', 'username', 'email', 'password')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = USER_MODEL.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
