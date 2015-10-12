from django.views.generic.detail import DetailView

from .models import Teacher


class TeachersDetailView(DetailView):
    model = Teacher
    template_name = "teacher_detail.html"
    context_object_name = 'teacher'
    lookup_field = "slug"
