from django.db import models


# Create your models here.
# python manage.py makemigrations
# python manage.py migrate
class File(models.Model):
    filename = models.CharField(max_length=128)
    downloads = models.IntegerField(default=0)
    max_downloads = models.IntegerField(default=1)
    size = models.IntegerField('File Size')
    mime_type = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.filename}'

