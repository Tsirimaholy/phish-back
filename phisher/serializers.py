from rest_framework import serializers

from .models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'password', 'login_date']
    login_date = serializers.DateTimeField(read_only=True)

