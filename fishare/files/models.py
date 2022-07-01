import string
from random import choices

from django.conf import settings
from django.db import models
from django.urls import reverse


def slugify():
    return ''.join(choices(string.ascii_letters + string.digits, k=settings.SLUG_LENGTH))


# Create your models here.
# python manage.py makemigrations
# python manage.py migrate
class File(models.Model):
    slug = models.CharField(default=slugify, max_length=settings.SLUG_LENGTH, unique=True, null=None, editable=False)
    filename = models.CharField(max_length=128, editable=False)
    downloads = models.IntegerField(default=0, editable=False)
    max_downloads = models.IntegerField(default=1)
    size = models.IntegerField('File Size', editable=False)
    mime_type = models.CharField(max_length=64, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(null=False, )

    def save(self, *args, **kwargs):
        if self.id is None:
            # set the metadata based on uploaded file
            self.filename = self.file.name
            self.mime_type = self.file.file.content_type
            self.size = self.file.size

            # renaming the file on filesystem
            self.file.name = self.slug

        super().save(args, kwargs)

    def delete(self, *args, **kwargs):
        # delete from filesystem first
        path = settings.MEDIA_ROOT / self.filename
        path.unlink(missing_ok=True)

        # delete from db
        super().delete(args, kwargs)

    def __str__(self):
        return f'{self.filename}'

    def get_absolute_url(self):
        return reverse('files:download_file', kwargs={'slug': self.slug})

    def get_formatted_filesize(self, suffix="B"):
        size = 0
        if self.size:
            size = self.size
        for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
            if abs(size) < 1024.0:
                return f"{size:3.1f}{unit}{suffix}"
            size /= 1024.0
        return f"{size:.1f}Yi{suffix}"

    get_formatted_filesize.short_description = 'Size'
