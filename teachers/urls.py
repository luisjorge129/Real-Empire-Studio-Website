from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^maestros/(?P<slug>[\w-]+)/$',
    	views.TeachersDetailView.as_view(),
    	name='teachers_detail'),
]
