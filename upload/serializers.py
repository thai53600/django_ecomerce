from . import models
from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = (
            'id',
            'url',
            'width',
            'height',
            'filename',
            'format',
            'created_at'
        )
