from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name', 'description', 'time',
              'image', 'facebook', 'twitter',
              'google_plus', 'status')
    list_display = ('id', 'name', 'time',
                    'status', 'created_date',
                    'updated_date')
    list_display_links = ['id', 'name', 'time']
    list_filter = ['status']
    search_fields = ['id', 'name',
                     'time', 'description']


admin.site.register(Event, EventAdmin)
