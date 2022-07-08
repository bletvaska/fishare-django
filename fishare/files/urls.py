from django.urls import path

from fishare.files import views

from fishare.files.api.viewsets import FileViewSet

app_name = 'files'

urlpatterns = [
    path(
        '<str:slug>',
        views.download_file,
        name='download_file'
    ),
    path('dummy/', views.homepage, name='dummy'),
    path('', views.FileUploadView.as_view(), name='homepage'),
    path('files/', views.FilesListView.as_view(), name='list-files'),
    path('cron/', views.delete_outdated_files, name='cron'),

    # path('api/files/', FileListAPIView.as_view(), name='list')
    path('api/files/', FileViewSet.as_view({'get': 'list', 'post': 'create'}), name='viewset')
]
