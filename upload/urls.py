from django.urls import path
from upload import views

urlpatterns = [
    path("upload-image/", views.PhotoAPIView.as_view()),
    path("upload-multiple-image/", views.UploadMultipleImagesAPIView.as_view()),
]
