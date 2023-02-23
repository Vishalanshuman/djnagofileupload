from django.urls import path
from . views import FileUploadView, filesDetailView, secureView,loginView, signupView

urlpatterns = [
    path('', FileUploadView, name='file'),
    path('file/', filesDetailView, name="file_detail"),
    path('login/', loginView, name="Login"),
    path('signup/', signupView, name="signup"),

    path('logout/', loginView, name="logout"),


    path('media/files__/<str:file>', secureView, name='secure')
]
