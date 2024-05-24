from rest_framework import views
from backend_ecommerce.helpers import custom_response
from rest_framework.permissions import AllowAny
import cloudinary
from .models import Photo
from .serializers import PhotoSerializer


class PhotoAPIView(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        
        try:
            photos = Photo.objects.all()
            serializers = PhotoSerializer(photos, many=True)
            return custom_response('Get all photos successfully!', 'Success', serializers.data, 200)
        except:
            return custom_response('Get al  l photos failed!', 'Error', None, 400)

    def post(self, request):
        if 'uploadImage' not in request.FILES:
            return custom_response('No upload resource', 'Error', 'No image file found in request', 400)
            
        if request.method == 'POST':
            try:
                image = request.FILES['uploadImage']
                upload_result = cloudinary.uploader.upload(image)
                image = Photo (
                    id=upload_result['public_id'],
                    url=upload_result['secure_url'],
                    filename=upload_result['original_filename'],
                    format=upload_result['format'],
                    width=upload_result['width'],
                    height=upload_result['height'],
                    created_at=upload_result['created_at'],
                )
                image.save()
                serializer = PhotoSerializer(image)
                
                return custom_response('Upload image successfully!', 'Success', serializer.data, 200)
            except  Exception as e:
                return custom_response('Upload image failed!', 'Error', [str(e)], 400)
        
class UploadMultipleImagesAPIView(views.APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        if 'uploadImage' not in request.FILES:
            return custom_response('No upload resource', 'Error', 'No image file found in request', 400)
            
        if request.method == 'POST':
            images = request.FILES.getlist('uploadImage')
            data = []
            for image in images: 
                try:
                    upload_result = cloudinary.uploader.upload(image)
                    img_obj = Photo (
                        id=upload_result['public_id'],
                        url=upload_result['secure_url'],
                        filename=upload_result['original_filename'],
                        format=upload_result['format'],
                        width=upload_result['width'],
                        height=upload_result['height'],
                        created_at=upload_result['created_at'],
                    )
                    img_obj.save()
                    serializer = PhotoSerializer(img_obj)
                    data.append(serializer.data)
                except  Exception as e:
                    return custom_response('Upload image failed!', 'Error', [str(e)], 400)
                    
            return custom_response('Upload images successfully!', 'Success', data, 200)
