from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^maestros/$',
    	views.TeachersListView.as_view(),
    	name='teachers_list'),
    url(r'^maestro/(?P<slug>[\w-]+)/$',
    	views.TeachersDetailView.as_view(),
    	name='teachers_detail'),
    url(r'^clases/$', views.ClassView.as_view(),
    	name='class'),
    url(r'^api/maestros/$',
    	views.ApiTeacherListView.as_view(),
    	name='teachers_list_api'),
    url(r'^api/maestro/(?P<slug>[\w-]+)/$',
    	views.ApiTeachersDetailView.as_view(),
    	name='teachers_detail_api'),
    url(r'^api/clases/$', views.ApiClassList.as_view(),
        name='class_list_api'),
    url(r'^precios/$', views.PriceView.as_view(),
        name='price'),
]
