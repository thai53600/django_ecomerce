from rest_framework import views, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import Http404
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from .helpers import custom_response, parse_request


# Create your views here.
class CategoryAPIView(views.APIView):

    def get(self, request):
        try:
            categories = Category.objects.all()
            serializers = CategorySerializer(categories, many=True)
            return custom_response('Get all categories successfully!', 'Success', serializers.data, 200)
        except:
            return custom_response('Get all categories failed!', 'Error', None, 400)

    def post(self, request):
        data = parse_request(request)        
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return custom_response('Create category successfully!', 'Success', serializer.data, 201)
        else:
            return custom_response('Create category failed', 'Error', serializer.errors, 400)


class CategoryDetailAPIView(views.APIView):
    
    def get_object(self, id_slug):
        try:
            return Category.objects.get(id=id_slug)
        except:
            raise Http404
        
    def get(self, request, id_slug, format=None):
        try:
            category = self.get_object(id_slug)
            serializer = CategorySerializer(category)
            return custom_response('Get category successfully!', 'Success', serializer.data, 200)
        except:
            return custom_response('Get category failed!', 'Error', "Category not found!", 400)
    
    def put(self, request, id_slug):
        try:
            data = parse_request(request)
            category = self.get_object(id_slug)
            serializer = CategorySerializer(category, data=data)
            if serializer.is_valid():
                serializer.save()
                return custom_response('Update category successfully!', 'Success', serializer.data, 200)
            else:
                return custom_response('Update category failed', 'Error', serializer.errors, 400)
        except:
            return custom_response('Update category failed', 'Error', "Category not found!", 400)
        
    def delete(self, request, id_slug):
        try:
            category = self.get_object(id_slug)
            category.delete()
            return custom_response('Delete category successfully!', 'Success', { "category_id": id_slug }, 204)
        except:
            return custom_response('Delete category failed!', 'Error', "Category not found!", 400)
    

class ProductViewAPI(views.APIView):
    
    def get(self, request):
        try:
            products = Product.objects.all()
            serializers = ProductSerializer(products, many=True)
            return custom_response('Get all products successfully!', 'Success', serializers.data, 200)
        except:
            return custom_response('Get all products failed!', 'Error', None, 400)
        
    def post(self, request):
        try:
            data = parse_request(request)
            category = Category.objects.get(id=data['category_id'])
            product = Product(
                name=data['name'],
                unit=data['unit'],
                price=data['price'],
                discount=data['discount'],
                amount=data['amount'],
                thumbnail=data['thumbnail'],
                category_id=category    
            )
            product.save()
            serializer = ProductSerializer(product)
            return custom_response('Create product successfully!', 'Success', serializer.data, 201)
        except Exception as e:
            return custom_response('Create product failed', 'Error', { "error": str(e) }, 400)
        

class ProductDetailAPIView(views.APIView):
    
    def get_object(self, id_slug):
        try:
            return Product.objects.get(id=id_slug)
        except:
            raise Http404
        
    def get(self, request, id_slug, format=None):
        try:
            product = self.get_object(id_slug)
            serializer = ProductSerializer(product)
            return custom_response('Get product successfully!', 'Success', serializer.data, 200)
        except:
            return custom_response('Get product failed!', 'Error', "Product not found!", 400)
    
    def put(self, request, id_slug):
        try:
            data = parse_request(request)
            product = self.get_object(id_slug)
            serializer = ProductSerializer(product, data=data)
            if serializer.is_valid():
                serializer.save()
                return custom_response('Update product successfully!', 'Success', serializer.data, 200)
            else:
                return custom_response('Update product failed', 'Error', serializer.errors, 400)
        except:
            return custom_response('Update product failed', 'Error', "Category not found!", 400)
        
    def delete(self, request, id_slug):
        try:
            product = self.get_object(id_slug)
            product.delete()
            return custom_response('Delete product successfully!', 'Success', { "product_id": id_slug }, 204)
        except:
            return custom_response('Delete product failed!', 'Error', "Product not found!", 400)