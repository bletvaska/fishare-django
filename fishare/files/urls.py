from django.urls import path

from fishare.files import views

app_name = 'files'

urlpatterns = [
    path(
        '<str:slug>',
        views.download_file,
        name='download_file'
    ),
    path('', views.homepage, name='homepage'),
    path('upload/', views.FileUploadView.as_view(), name='upload'),
]
