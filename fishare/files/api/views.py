from django.db.models import F
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView

from .serializers import FileSerializer, FileHyperlinkedSerializer
from ..models import File


class FileListAPIView(ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    # queryset = File.objects.filter(downloads__lt=F('max_downloads'))


class FileDetailView(RetrieveAPIView):
    model = File
    serializer_class = FileHyperlinkedSerializer
    queryset = File.objects.filter(downloads__lt=F('max_downloads'))
    lookup_field = 'slug'
