from . import models
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Product
        fields = (
            'id',
            'name',
            'unit',
            'price',
            'discount',
            'amount',
            'is_public',
            'thumbnail',
            'category_id',
            'created_at',
            'updated_at',
            'deleted_at'
        )
        
class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = models.Category
        fields = (
            'id',
            'name',
            'slug',
            'icon_url',
            'products',
            'created_at',
            'updated_at',
            'deleted_at'
        )
