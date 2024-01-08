from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, DateTimeField, IntegerField


class CategorySerializer(serializers.ModelSerializer):
    id = IntegerField(required=False)
    name = CharField(required=True)
    slug = CharField(required=True)
    icon_url = CharField(required=True)
    created_at = DateTimeField(required=False)
    updated_at = DateTimeField(required=False)
    deleted_at = DateTimeField(required=False)
    
    class Meta:
        model = models.Category
        fields = (
            'id',
            'name',
            'slug',
            'icon_url',
            'created_at',
            'updated_at',
            'deleted_at'
        )
