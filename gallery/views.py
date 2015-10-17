from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Video
from .models import Gallery


class VideoListView(ListView):
    model = Video
    template_name = "videos_list.html"
    context_object_name = 'videos'


class GalleryListView(ListView):
    model = Gallery
    template_name = "gallery_list.html"
    context_object_name = 'galleries'