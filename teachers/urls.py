from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^maestros/$',
    	views.TeachersListView.as_view(),
    	name='teachers_list'),
    url(r'^maestros/(?P<slug>[\w-]+)/$',
    	views.TeachersDetailView.as_view(),
    	name='teachers_detail'),
]
