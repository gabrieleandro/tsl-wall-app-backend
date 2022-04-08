from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from .serializers import UserSerializer


# Get the User Model
User = get_user_model()


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny,]
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
