from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .views import RepublicCardViewSet, PersonalCardViewSet, MyPersonalCards, MyRepublicCards, UpdateCard
from rest_framework import routers

urlpatterns = [
    path('mycards/',MyPersonalCards.as_view()),
    path('myrepubliccards/',MyRepublicCards.as_view()),
    path('update/<int:card_id>/', UpdateCard.as_view()),
   ] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
