from django.urls import path

from fishare.files import views

app_name = 'files'

urlpatterns = [
    path(
        '<str:slug>',
        views.download_file,
        name='download_file'
    ),
    path('dummy/', views.homepage, name='dummy'),
    path('', views.FileUploadView.as_view(), name='homepage'),
    path('files/', views.FilesListView.as_view(), name='list'),
]
