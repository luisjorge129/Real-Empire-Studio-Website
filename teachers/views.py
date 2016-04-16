from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from .models import Teacher
from .models import Class
# from .models import Price
from .serializers import TeacherSerializer
from .serializers import ClassSerializer

from rest_framework import generics
from django_filters import FilterSet
from rest_framework import filters


class ApiTeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.filter(status=True)
    serializer_class = TeacherSerializer
    page_size = 0


class ApiTeachersDetailView(generics.RetrieveAPIView):
    queryset = Teacher.objects.filter(status=True)
    serializer_class = TeacherSerializer
    lookup_field = 'slug'


class ClassFilter(FilterSet):
    class Meta:
        model = Class
        fields = ['day', ]


class ApiClassList(generics.ListAPIView):
    queryset = Class.objects.filter(status=True).order_by('start_time')
    serializer_class = ClassSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ClassFilter
    page_size = 0
    order_by = 'start_time'


class TeachersListView(ListView):
    queryset = Teacher.objects.filter(status=True)
    template_name = "teachers_list.html"
    context_object_name = 'teachers'


class TeachersDetailView(DetailView):
    queryset = Teacher.objects.filter(status=True)
    template_name = "teacher_detail.html"
    context_object_name = 'teacher'
    lookup_field = "slug"


class ClassView(ListView):
    queryset = Class.objects.filter(status=True)
    template_name = "class.html"
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = {}
        context['monday_list'] = Class.objects.filter(
            status=True, day='Monday').order_by('start_time')
        context['tuesday_list'] = Class.objects.filter(
            status=True, day='Tuesday').order_by('start_time')
        context['wednesday_list'] = Class.objects.filter(
            status=True, day='Wednesday').order_by('start_time')
        context['thursday_list'] = Class.objects.filter(
            status=True, day='Thursday').order_by('start_time')
        context['friday_list'] = Class.objects.filter(
            status=True, day='Friday').order_by('start_time')
        context['saturday_list'] = Class.objects.filter(
            status=True, day='Saturday').order_by('start_time')
        return context


class PriceView(TemplateView):
    template_name = "price.html"
