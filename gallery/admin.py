from django.contrib import admin

from .models import Video

class VideoAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name', 'description', 'status')
    list_display = ('id', 'name', 'description', 'status',
    				'created_date', 'updated_date')
    list_display_links = ['id', 'name']
    list_filter = ['status']
    search_fields = ['id', 'name']


admin.site.register(Video, VideoAdmin)
