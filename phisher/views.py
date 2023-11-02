from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import UserInfo
from .serializers import UserInfoSerializer


@api_view(['GET', 'POST'])
def users(request):
    if request.method == "POST":
        serializer = UserInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    elif request.method == "GET":
        users = UserInfo.objects.all()
        serializer = UserInfoSerializer(users, many=True)
        return Response(data=serializer.data)
