from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from fishare.files.models import File


# admin.site.register(File)

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['filename', 'mime_type', 'get_formatted_filesize', 'get_downloads', 'created_at', 'download_link']
    ordering = ['-created_at']
    list_filter = ['mime_type']
    search_fields = ['filename']

    def get_downloads(self, file: File):
        return f'{file.downloads}/{file.max_downloads}'

    get_downloads.short_description = 'Downloads'

    def download_link(self, file: File):
        return format_html(f'<a href="{file.get_absolute_url()}">{file.slug}</a>')

    download_link.short_description = 'Download'
