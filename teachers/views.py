from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Teacher


class TeachersListView(ListView):
    model = Teacher
    template_name = "teachers_list.html"
    context_object_name = 'teachers'


class TeachersDetailView(DetailView):
    model = Teacher
    template_name = "teacher_detail.html"
    context_object_name = 'teacher'
    lookup_field = "slug"
