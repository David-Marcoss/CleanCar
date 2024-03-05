
from rest_framework import viewsets, permissions

from ..models import User
from .serializers import Userserializer

from rest_framework import viewsets, permissions
from rest_framework import generics

from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import PermissionDenied

class UserCreateViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):

        data = request.data.copy()

        user = self.get_serializer(data=data)
        user.is_valid(raise_exception=True)
        user = user.save()

        return Response(self.get_serializer(user).data, status=status.HTTP_201_CREATED)


class UserViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        
        object = User.objects.get(pk=self.kwargs['pk'])

        if self.request.auth.key == Token.objects.get(user=object).key:
            return object
        
        raise PermissionDenied('Usuário não autorizado!!!')

    def update(self, request, *args, **kwargs):

        data = request.data.copy()
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)