from rest_framework.viewsets import ModelViewSet

from .serializers import FileSerializer
from ..models import File


class FileViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing files.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
