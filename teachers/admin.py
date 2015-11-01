from django.contrib import admin

from .models import Teacher
from .models import Class


class TeacherAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fieldsets = (
                ('Personal Information', {'fields':
                        ('name', 'biography',
                         'image', 'course')}),
                ('Social Networks',
                    {'fields': ('facebook', 'twitter',
                                'google_plus', 'instagram')}),
                ('Permission',
                    {'fields': ('status',)}),
                )
    list_display = ('id', 'name', 'facebook',
                    'twitter', 'google_plus',
                    'instagram', 'status',
                    'created_date', 'updated_date')
    list_display_links = ['id', 'name']
    list_filter = ['course', 'status']
    search_fields = ['id', 'name', 'courses']
    filter_horizontal = ('course',) 


class ClassAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fieldsets = (
                ('Course Information', {'fields':
                    ('name', ('day', 'start_time', 
                'end_time'), 'status')}),
                )
    list_display = ('id', 'name', 'day',
                    'start_time', 'end_time', 'status',
    				'created_date', 'updated_date')
    list_display_links = ['id', 'name', 'day',
                          'start_time', 'end_time']
    list_filter = ['status']
    search_fields = ['id', 'name',
                     'start_time', 'end_time']


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Class, ClassAdmin)
