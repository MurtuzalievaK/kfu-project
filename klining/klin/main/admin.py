from django.contrib import admin
from django.utils.html import format_html

from .models import New

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100"/>', obj.image.url)
        else:
            return '(No image)'

    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'



admin.site.register(New)
