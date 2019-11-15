from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .views import CreatePerson

urlpatterns = [
    path('create/',CreatePerson.as_view()),
   ] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
