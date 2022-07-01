from django.urls import path

from fishare.error_handlers.views import not_found_view

urlpatterns = [
    path('404/', not_found_view)
]

handler404 = 'fishare.error_handlers.views.not_found_view'
