from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Photo(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    url = models.CharField(max_length=255)
    image = CloudinaryField('image')
    filename = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)