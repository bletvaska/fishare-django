from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from fishare.files.models import File


def download_file(request, slug: str):
    print(f'>> downloading file {slug}')
    # file = get_object_or_404(File, slug=slug)
    # TODO rozsirit podmienku na kontrolu vyrazu downloads < max_downloads
    file = File.objects.get(slug=slug)

    if file.downloads >= file.max_downloads:
        return HttpResponse('Max downloads reached!', status=404)

    # update downloads
    file.downloads += 1
    file.save()

    # prepare response
    response = HttpResponse(file.file, content_type=file.mime_type)
    response['Content-Disposition'] = f'attachment; filename={file.filename}'

    return response


def homepage(request):
    return render(request, 'homepage.html')

