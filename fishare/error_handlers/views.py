from django.shortcuts import render


# Create your views here.
def not_found_view(request, exception=None):
    return render(request, '404.html', status=404)


def server_error_view(request, exception=None):
    return render(request, '500.html', status=500)
