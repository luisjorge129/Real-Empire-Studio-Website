from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^video/$', views.VideoListView.as_view(),
    	name='video_list'),
	url(r'^gallery/$', views.GalleryListView.as_view(),
    	name='video_list'),
    
]
