from django.db.models import F
from django.http import FileResponse
from django.shortcuts import render

from fishare.files.models import File


def download_file(request, slug: str):
    # SELECT * FROM file where downloads < max_downloads AND slug='xxxx';
    file = File.objects.filter(downloads__lt=F('max_downloads')).get(slug=slug)

    # update downloads
    file.downloads += 1
    file.save()

    # prepare response
    return FileResponse(file.file, as_attachment=True, filename=file.filename)


def homepage(request):
    context = {
        "something": "this is bjutifuľ.",
        "files": File.objects.all(),
    }
    return render(request, 'homepage.html', context)
