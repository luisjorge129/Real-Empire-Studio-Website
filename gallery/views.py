from django.shortcuts import render
from django.views.generic.list import ListView

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import django_filters

from .models import Video
from .models import VideoCategory
from .models import Gallery
from .models import GalleryCategory


class VideoFilter(django_filters.FilterSet):
    class Meta:
        model = Video
        fields = ['category__name',]


class VideoListView(ListView):
    model = Video
    template_name = "videos_list.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        try:
            page = self.request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        objects = VideoFilter(self.request.GET,
                              queryset=Video.objects.filter(status=True))

        p = Paginator(objects, 12)

        page_obj = p.page(page)

        categories = VideoCategory.objects.all()


        context = {
            'page_obj': page_obj,
            'categories_list': categories
        }

        context.update(kwargs)

        return context


class GalleryListView(ListView):
    model = Gallery
    template_name = "gallery_list.html"
    context_object_name = 'galleries'
