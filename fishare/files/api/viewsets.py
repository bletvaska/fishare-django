from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import FileSerializer, FileHyperlinkedSerializer, FileDetailHyperlinkedSerializer
from ..models import File


class FileViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing files.
    """
    queryset = File.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FileDetailHyperlinkedSerializer

        return FileHyperlinkedSerializer
