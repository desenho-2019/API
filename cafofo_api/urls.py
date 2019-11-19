"""cafofo_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from cards.views import RepublicCardViewSet, PersonalCardViewSet
from republic.views import RepublicViewSet
from person.views import PersonViewSet
from vacancy.views import VacancyViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('cards/republic', RepublicCardViewSet)
router.register('cards/personal', PersonalCardViewSet)
router.register('republic/all', RepublicViewSet)
router.register('person/all', PersonViewSet)
router.register('vacancy/all', VacancyViewSet)



# router.register('republic/<pk>', RepublicViewSet)
# router.register('republic/<republic_id>', RepublicDetail)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/',include('users.urls')),
    path('person/',include('person.urls')),
    path('republic/',include('republic.urls')),
    path('cards/',include('cards.urls')),
    path('vacancy/',include('vacancy.urls')),
   ] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
