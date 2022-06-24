import string
from random import choices

from django.conf import settings
from django.db import models


def slugify(length=7):
    return ''.join(choices(string.ascii_letters + string.digits, k=length))


# Create your models here.
# python manage.py makemigrations
# python manage.py migrate
class File(models.Model):
    slug = models.CharField(default=slugify, max_length=7, unique=True, null=None)
    filename = models.CharField(max_length=128, editable=False)
    downloads = models.IntegerField(default=0, editable=False)
    max_downloads = models.IntegerField(default=1)
    size = models.IntegerField('File Size', editable=False)
    mime_type = models.CharField(max_length=64, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(null=False)

    def save(self, *args, **kwargs):
        print(args)
        print(kwargs)
        # if self.id is None:
        self.filename = self.file.name
        self.size = self.file.size
        # if type(self.file.file) != BufferedReader:
        self.mime_type = self.file.file.content_type

        super().save(args, kwargs)

    def delete(self, *args, **kwargs):
        # delete from filesystem first
        path = settings.MEDIA_ROOT / self.filename
        path.unlink(missing_ok=True)

        # delete from db
        super().delete(args, kwargs)

    def __str__(self):
        return f'{self.filename}'
