from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .views import RepublicCardViewSet, PersonalCardViewSet, MyPersonalCards
from rest_framework import routers

urlpatterns = [
    path('mycards/',MyPersonalCards.as_view()),
    path('myrepubliccards/',MyRepublicCards.as_view()),

   ] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

router = routers.DefaultRouter()
router.register('republic/', RepublicCardViewSet)
router.register('personal/', PersonalCardViewSet)
