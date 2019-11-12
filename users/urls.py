from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

from users.views import  ExampleView,  ListUser, CreateUser,UserUpdateDeleteSet
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView





urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('exemple/', ExampleView.as_view()),
    path('list/',ListUser.as_view()),
    path('create/',CreateUser.as_view()),
    path('settings/<int:pk>/',UserUpdateDeleteSet.as_view()),
   ] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
