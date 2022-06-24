from django.contrib import admin

# Register your models here.
from fishare.files.models import File


# admin.site.register(File)

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['filename', 'mime_type', 'size', 'get_downloads', 'created_at']
    ordering = ['-created_at']
    list_filter = ['mime_type']
    search_fields = ['filename']

    def get_downloads(self, file: File):
        return f'{file.downloads}/{file.max_downloads}'

    get_downloads.short_description = 'Downloads'
