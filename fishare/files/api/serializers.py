from rest_framework.serializers import ModelSerializer

from ..models import File


class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ['filename', 'size', 'mime_type', 'slug', 'file']
