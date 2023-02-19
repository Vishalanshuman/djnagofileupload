from django.urls import path
from . views import FileUploadView, filesDetailView, secureView

urlpatterns = [
    path('', FileUploadView, name='file'),
    path('file/', filesDetailView, name="file_detail"),
    path('media/files__/<str:file>', secureView, name='secure')
]
