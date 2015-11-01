from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Teacher
from .models import Class


class TeachersListView(ListView):
    model = Teacher
    template_name = "teachers_list.html"
    context_object_name = 'teachers'


class TeachersDetailView(DetailView):
    model = Teacher
    template_name = "teacher_detail.html"
    context_object_name = 'teacher'
    lookup_field = "slug"


class ClassView(ListView):
    model = Class
    template_name = "class.html"
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = {}
        context['monday_list'] = Class.objects.filter(status=True, day='Monday')
        context['tuesday_list'] = Class.objects.filter(status=True, day='Tuesday')
        context['wednesday_list'] = Class.objects.filter(status=True, day='Wednesday')
        context['thursday_list'] = Class.objects.filter(status=True, day='Thursday')
        context['friday_list'] = Class.objects.filter(status=True, day='Friday')
        context['saturday_list'] = Class.objects.filter(status=True, day='Saturday')
        # print context['saturday_list'].teachers
        return context
