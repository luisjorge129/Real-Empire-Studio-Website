from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^maestros/$',
    	views.TeachersListView.as_view(),
    	name='teachers_list'),
    url(r'^maestro/(?P<slug>[\w-]+)/$',
    	views.TeachersDetailView.as_view(),
    	name='teachers_detail'),
    url(r'^clases/$', views.ClassView.as_view(), name='class'),
]
