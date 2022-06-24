from django.contrib import admin

# Register your models here.
from fishare.files.models import File


# admin.site.register(File)

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['filename', 'mime_type', 'format_filesize', 'get_downloads', 'created_at']
    ordering = ['-created_at']
    list_filter = ['mime_type']
    search_fields = ['filename']

    def get_downloads(self, file: File):
        return f'{file.downloads}/{file.max_downloads}'

    get_downloads.short_description = 'Downloads'

    def format_filesize(self, file: File, suffix="B"):
        size = 0
        if file.size:
            size = file.size
        for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
            if abs(size) < 1024.0:
                return f"{size:3.1f}{unit}{suffix}"
            size /= 1024.0
        return f"{size:.1f}Yi{suffix}"

    format_filesize.short_description = 'Size'
