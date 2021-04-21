from rest_framework import views, status, viewsets, filters
from rest_framework.response import Response

from api.models import MaskDetector

from api.serializers import MaskDetectorSerializer

class MaskDetectorViewSet(viewsets.ModelViewSet):
    queryset = MaskDetector.objects.all()
    serializer_class = MaskDetectorSerializer