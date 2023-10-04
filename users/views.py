from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,)

from users.models import User
from permissions import IsOwner, IsAuthenticated
from users.serializers import UserSerializer


class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner, IsAuthenticated]
