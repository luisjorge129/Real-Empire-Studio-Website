from django.views.generic.list import ListView

from pure_pagination import Paginator, PageNotAnInteger
from django_filters import FilterSet
from rest_framework import filters
from rest_framework import generics

from .serializers import VideoListSerializer
from .serializers import GalleryListSerializer
from .models import Video
from .models import VideoCategory
from .models import Gallery
from .models import GalleryCategory


class VideoFilter(FilterSet):
    class Meta:
        model = Video
        fields = ['category__name', 'video_type']


class GalleryFilter(FilterSet):
    class Meta:
        model = Gallery
        fields = ['category__name']


class ApiVideoList(generics.ListAPIView):
    queryset = Video.objects.filter(status=True)
    serializer_class = VideoListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = VideoFilter


class ApiGalleryList(generics.ListAPIView):
    queryset = Gallery.objects.filter(status=True)
    serializer_class = GalleryListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = GalleryFilter


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
    paginate_by = 12

    def get_context_data(self, **kwargs):
        try:
            page = self.request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        objects = GalleryFilter(self.request.GET,
                                queryset=Gallery.objects.filter(status=True))

        p = Paginator(objects, 12)

        page_obj = p.page(page)

        categories = GalleryCategory.objects.all()

        context = {
            'page_obj': page_obj,
            'categories_list': categories
        }

        context.update(kwargs)

        return context
