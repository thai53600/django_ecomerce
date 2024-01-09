from rest_framework import views
from backend_ecommerce.helpers import custom_response, parse_request
from .serializers import PhotoSerializer
from .models import Photo
import cloudinary


# Create your views here.
class PhotoAPIView(views.APIView):

    def get(self, request):
        try:
            photos = Photo.objects.get()
            print('photos', photos)
            serializers = PhotoSerializer(photos, many=True)
            return custom_response('Get all photos successfully!', 'Success', serializers.data, 200)
        except:
            return custom_response('Get all photos failed!', 'Error', None, 400)

    def post(self, request):
        if request.method == 'POST':
            try:
                image = request.FILES['image']
                print('image', image)
                
                # Use the Cloudinary uploader to upload the image.
                upload_result = cloudinary.uploader.upload(image)
                print('upload_result', upload_result)
                image = Photo (
                    id=upload_result['public_id'],
                    url=upload_result['secure_url'],
                    filename=upload_result['original_filename'],
                    created_at=upload_result['created_at'],
                    # image=upload_result['image'],
                )
                print('image', image)
                try:
                    image.save()
                except Exception as e:  
                    print('e', str(e))
                    return custom_response('Upload image failed!', 'Error', str(e), 400)
                return custom_response('Upload image successfully!', 'Success', upload_result, 200)
            except  Exception as e:
                return custom_response('Upload image failed!', 'Error', str(e) , 400)
        
        