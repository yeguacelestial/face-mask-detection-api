import os

from rest_framework import views, status, viewsets, filters
from rest_framework.response import Response

from api.models import MaskDetector

from api.serializers import MaskDetectorSerializer

from django.conf import settings

class MaskDetectorViewSet(viewsets.ModelViewSet):
    queryset = MaskDetector.objects.all()
    serializer_class = MaskDetectorSerializer

    def create(self, request):
        serializer = MaskDetectorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            image_dir = os.path.join(settings.MEDIA_ROOT, 'Images', str(request.data['image']))
            print(f"IMAGE DIR => {image_dir}")
            print(f"EXISTS? => {os.path.exists(image_dir)}")

            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)