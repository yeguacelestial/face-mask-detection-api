from django.urls import path, include

from api.views import MaskDetectorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('mask-detection', MaskDetectorViewSet)

urlpatterns = [
    path('', include(router.urls))
]