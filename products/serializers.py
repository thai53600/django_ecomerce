from . import models
from rest_framework import serializers


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = (
            'id',
            'product_id',
            'image_url',
            'created_at',
            'updated_at',
            'deleted_at'
        )
        
class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductComment
        fields = (
            'id',
            'rating',
            'comment',
            'product_id',
            'user_id',
            'parent_id',
            'created_at',
            'updated_at',
            'deleted_at'
        )
        
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    comments = ProductCommentSerializer(many=True, read_only=True)
    
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
            'images',
            'comments',
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
