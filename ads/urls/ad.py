from django.contrib import admin
from django.urls import path
from rest_framework import routers

from ads.views.ad import AdImageUpload, AdViewSet

router = routers.SimpleRouter()
router.register('', AdViewSet)


urlpatterns = [
    path('<int:pk>/upload_image/', AdImageUpload.as_view())
]

urlpatterns += router.urls