from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^videos/$', views.VideoListView.as_view(),
        name='video_list'),
    url(r'^fotos/$', views.GalleryListView.as_view(),
        name='image_list'),
    url(r'^api/videos/$', views.ApiVideoList.as_view(),
        name='api_video_list'),
]
