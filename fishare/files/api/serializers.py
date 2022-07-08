from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from ..models import File


class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ['filename', 'size', 'mime_type', 'slug', 'file']


class FileHyperlinkedSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ['url', 'filename', 'size', 'file']
        extra_kwargs = {
            'url': {
                'view_name': 'files:api-single',
                'lookup_field': 'slug'
            }
        }


class FileDetailHyperlinkedSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ['url', 'filename', 'size', 'file', 'mime_type', 'created_at', 'updated_at', 'downloads',
                  'max_downloads']
        extra_kwargs = {
            'url': {
                'view_name': 'files:api-single',
                'lookup_field': 'slug'
            }
        }
