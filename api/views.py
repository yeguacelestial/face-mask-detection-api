import os

from rest_framework import views, status, viewsets, filters
from rest_framework.response import Response

from api.models import MaskDetector

from api.serializers import MaskDetectorSerializer

from django.conf import settings

from load_model import predict_mask_on_img


class MaskDetectorViewSet(viewsets.ModelViewSet):
    queryset = MaskDetector.objects.all()
    serializer_class = MaskDetectorSerializer

    def create(self, request):
        serializer = MaskDetectorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            image_dir = os.path.join(settings.MEDIA_ROOT, 'Images', str(request.data['image']))

            # Predict mask on img
            result = predict_mask_on_img(image_dir)

            response_data = {
                'person_has_mask': result[0],
                'scalar_result': result[1]
            }

            serializer.validated_data['person_has_mask'] = result[0]
            serializer.save()

            return Response(status=status.HTTP_201_CREATED, data={'prediction_result': response_data})

        return Response(status=status.HTTP_400_BAD_REQUEST)