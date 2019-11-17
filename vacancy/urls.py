from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .views import CreateListCompositeView, CreateListLeafView, CreateListLeafCompositeView
from rest_framework import routers

urlpatterns = [
    path('<int:card_id>/composite', CreateListCompositeView.as_view()),
    path('<int:card_id>/leaf', CreateListLeafView.as_view()),
    path('<int:card_id>/<int:composite_id>/leaf', CreateListLeafCompositeView.as_view()),
    path('<int:card_id>/<int:composite_id>/composite', CreateListLeafCompositeView.as_view()),
    path('<int:card_id>/composite/<int:composite_id>', CreateListLeafView.as_view()),
   ] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
