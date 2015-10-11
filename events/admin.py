from django.contrib import admin

from .models import Event
from .models import Video

class EventAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name', 'time', 'teacher',
    		  'status')
    list_display = ('id', 'name', 'time', 'status',
    				'created_date', 'updated_date')
    list_display_links = ['id', 'name', 'time']
    list_filter = ['status']
    search_fields = ['id', 'name', 'time']


class VideoAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name', 'description', 'status')
    list_display = ('id', 'name', 'description', 'status',
    				'created_date', 'updated_date')
    list_display_links = ['id', 'name']
    list_filter = ['status']
    search_fields = ['id', 'name']


admin.site.register(Video, VideoAdmin)
admin.site.register(Event, EventAdmin)