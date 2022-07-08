from django.urls import path

from fishare.files import views

from fishare.files.api.views import FileListAPIView

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
]
