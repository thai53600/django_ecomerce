from . import models
from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = (
            'id',
            'url',
            'filename',
            'created_at'
        )
