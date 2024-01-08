from rest_framework import views, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import CategorySerializer
from .models import Category
from django.http import Http404


# Create your views here.
class CategoryAPIView(views.APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializers = CategorySerializer(categories, many=True)
        return Response(serializers.data)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = CategorySerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error", "message": "JSON decoding error"}, status=400)


class CategoryDetailAPIView(views.APIView):
    def get_object(self, id_slug):
        try:
            return Category.objects.get(id=id_slug)
        except:
            return Http404
        
    def get(self, request, id_slug, format=None):
        category = self.get_object(id_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self, request, id_slug):
        try:
            data = JSONParser().parse(request)
            category = self.get_object(id_slug)
            serializer = CategorySerializer(category, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error", "message": "JSON decoding error"}, status=400)
        
    def delete(self, request, id_slug):
        category = self.get_object(id_slug)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)