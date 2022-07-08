from rest_framework.generics import ListAPIView, ListCreateAPIView

from .serializers import FileSerializer
from ..models import File


class FileListAPIView(ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    # queryset = File.objects.filter(downloads__lt=F('max_downloads'))
