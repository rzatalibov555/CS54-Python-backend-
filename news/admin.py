from django.utils.html import format_html
from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_preview', 'time_create', 'time_update', 'is_published']
    list_editable = ["is_published"]
    list_display_links = ["title"]
    list_filter = ['is_published']
    search_fields = ['title']
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<a href="{}" target="_blank"><img src="{}" style="width: 100px; height: 70px; object-fit:cover;" /></a>',
                obj.image.url,
                obj.image.url
            )
        return "No Image"

admin.site.register(News, NewsAdmin)


