from rest_framework import serializers
from . import models
# import users.serializer as users_serializer


class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    def get_owner(self, instance):
        owner = instance.owner
        return owner.email
    class Meta:
        model = models.Property
        fields = '__all__'
