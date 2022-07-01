from django.db.models import F
from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from fishare.files.models import File


def download_file(request, slug: str):
    # SELECT * FROM file where downloads < max_downloads AND slug='xxxx';
    # file = File.objects.all()  # select * from file;
    # file = File.objects.get(slug=slug)  # select * from file where slug=slug
    # file = File.objects.filter(downloads__lt=F('max_downloads')).get(slug=slug)
    qs = File.objects.filter(downloads__lt=F('max_downloads')).filter(slug=slug)
    file = get_object_or_404(qs)

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


class FileUploadView(CreateView):
    model = File
    fields = ['file']
    # template_name = 'own_template.html'
