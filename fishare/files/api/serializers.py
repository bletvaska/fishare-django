from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from ..models import File


class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ['filename', 'size', 'mime_type', 'slug', 'file']


class FileHyperlinkedSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ['url', 'filename', 'size', ]
        extra_kwargs = {
            'url': {
                'view_name': 'files:api-single',
                'lookup_field': 'slug'
            }
        }
