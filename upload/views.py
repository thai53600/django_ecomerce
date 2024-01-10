from rest_framework import views
from backend_ecommerce.helpers import custom_response, parse_request
from .serializers import PhotoSerializer
from .models import Photo
import cloudinary


# Create your views here.
class PhotoAPIView(views.APIView):

    def get(self, request):
        try:
            photos = Photo.objects.all()
            print('photos', photos)
            serializers = PhotoSerializer(photos, many=True)
            return custom_response('Get all photos successfully!', 'Success', serializers.data, 200)
        except:
            return custom_response('Get all photos failed!', 'Error', None, 400)

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
                print(e)
                return custom_response('Upload image failed!', 'Error', str(e) , 400)
        
class UploadMultipleImagesAPIView(views.APIView):
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
                    print(e)
                    return custom_response('Upload image failed!', 'Error', str(e), 400)
                    
            return custom_response('Upload images successfully!', 'Success', data, 200)
        