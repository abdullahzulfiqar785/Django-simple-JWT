from rest_framework import permissions, serializers
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import PrivateSerializer, PublicSerializers
from .models import Public, Private

class PrivateApiView(ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = PrivateSerializer
    def get_queryset(self):
        Private.objects.create()
        return Private.objects.all()

class PublicApiView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PublicSerializers
    def get_queryset(self):
        return Public.objects.all()