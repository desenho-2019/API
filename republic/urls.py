from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .views import MyRepublic
from rest_framework import routers

urlpatterns = [
    path('new/',MyRepublic.as_view()),
   ] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
