from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, DateTimeField


class CategorySerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()
    name = CharField(source="name", required=True)
    slug = CharField(source="slug", required=True)
    icon_url = CharField(source="icon_url", required=False)
    created_at = DateTimeField(source="created_at", required=True)
    updated_at = DateTimeField(source="updated_at", required=True)
    deleted_at = DateTimeField(source="deleted_at", required=False)

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
