from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from fishare.files.models import File


def download_file(request, slug: str):
    print(f'>> downloading file {slug}')
    # file = get_object_or_404(File, slug=slug)
    file = File.objects.get(slug=slug)

    # update downloads
    file.downloads += 1
    file.save()


    return HttpResponse(f'>> downloading file {file}')
