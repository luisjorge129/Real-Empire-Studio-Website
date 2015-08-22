from django.contrib import admin

from .models import Subscribe


class SubscribeAdmin(admin.ModelAdmin):
    fields = ('email', )
    list_display = ('id', 'email',)
    list_display_links = ['id', 'email']
    search_fields = ['id', 'email']


admin.site.register(Subscribe, SubscribeAdmin)
