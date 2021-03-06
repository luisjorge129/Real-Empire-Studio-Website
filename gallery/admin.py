from django.contrib import admin

from .models import Video
from .models import VideoCategory
from .models import Gallery
from .models import GalleryCategory


class VideoAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('video_id', 'video_type',
              'name', 'description',
              'category', 'status')
    list_display = ('id', 'video_id', 'video_type', 'name',
                    'description', 'status',
                    'created_date', 'updated_date')
    list_display_links = ['id', 'video_id',
                          'video_type', 'name']
    list_filter = ['status']
    search_fields = ['id', 'name',
                     'video_id',
                     'description']
    filter_horizontal = ('category',)


class GalleryAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('image', 'name', 'description', 'category',
              'status')
    list_display = ('id', 'name', 'description', 'status',
                    'created_date', 'updated_date')
    list_display_links = ['id', 'name']
    list_filter = ['status']
    search_fields = ['id', 'name']
    filter_horizontal = ('category',)


class VideoCategoryAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name',)
    list_display = ('id', 'name', 'created_date',
                    'updated_date')
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


class GalleryCategoryAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name',)
    list_display = ('id', 'name', 'created_date',
                    'updated_date')
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


admin.site.register(Video, VideoAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(VideoCategory, VideoCategoryAdmin)
admin.site.register(GalleryCategory, GalleryCategoryAdmin)
