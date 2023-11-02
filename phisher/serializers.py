from rest_framework import serializers

from .models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'password', 'log_date']
    log_date = serializers.DateTimeField(read_only=True, source='loging_date')

