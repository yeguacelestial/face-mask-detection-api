from rest_framework import serializers
from api.models import MaskDetector

class MaskDetectorSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=False)
    person_has_mask = serializers.BooleanField()

    class Meta:
        model = MaskDetector
        fields = '__all__'