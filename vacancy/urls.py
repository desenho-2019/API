from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .views import CreateListCompositeView, CreateListLeafView, CreateListLeafCompositeView, UpdateVacancyStateView
from rest_framework import routers

urlpatterns = [
    path('<int:card_id>/composite', CreateListCompositeView.as_view()),
    path('<int:card_id>/leaf', CreateListLeafView.as_view()),
    path('<int:card_id>/<int:composite_id>/leaf', CreateListLeafCompositeView.as_view()),
    path('<int:card_id>/<int:vacancy_id>/updatestate/', UpdateVacancyStateView.as_view()),
   ] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
