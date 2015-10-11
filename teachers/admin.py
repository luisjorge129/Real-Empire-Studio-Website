from django.contrib import admin

from .models import Teacher
from .models import Course

class TeacherAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name', 'image', 'facebook',
    		  'twitter', 'instagram', 'course',
    		  'status')
    list_display = ('id', 'name', 'facebook',
    		  		'twitter', 'instagram', 'course',
    		  		'status', 'created_date', 'updated_date')
    list_display_links = ['id', 'name']
    list_filter = ['course', 'status']
    search_fields = ['id', 'name', 'courses']


class CourseAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name', 'time', 'status')
    list_display = ('id', 'name', 'time', 'status',
    				'created_date', 'updated_date')
    list_display_links = ['id', 'name', 'time']
    list_filter = ['status']
    search_fields = ['id', 'name']


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)