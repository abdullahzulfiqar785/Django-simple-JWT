from django.db import models
from rest_framework import fields, serializers
from .models import Private, Public


class PrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Private
        fields = '__all__'

class PublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Public
        fields = '__all__'