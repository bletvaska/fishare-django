from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import FileSerializer, FileHyperlinkedSerializer
from ..models import File


class FileViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing files.
    """
    queryset = File.objects.all()
    serializer_class = FileHyperlinkedSerializer
    lookup_field = 'slug'

    # def retrieve(self, request, slug=None):
    #     queryset = File.objects.all()
    #     file = get_object_or_404(queryset, slug=slug)
    #     serializer = FileHyperlinkedSerializer(file, context={'request': request})
    #     return Response(serializer.data)
