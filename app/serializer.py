from rest_framework import serializers
from . import models
# import users.serializer as users_serializer


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Property
        fields = '__all__'
