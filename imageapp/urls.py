from django.urls import path
from .views import image_upload, success, display_img, home, display_imag_2

urlpatterns = [
    path('image_upload/', image_upload.as_view(), name='upload'),
    path('success/', success, name='success'),
    path('display_image', display_img, name='display'),
    path('display_image_2',display_imag_2, name='display_2'),
    path('home', home, name='home'),
]