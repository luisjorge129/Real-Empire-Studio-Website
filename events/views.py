from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Event


class EventsListView(ListView):
	queryset = Event.objects.filter(status=True)
	template_name = "events_list.html"
	context_object_name = "events"


class EventsDetailView(DetailView):
	queryset = Event.objects.filter(status=True)
	template_name = "events_detail.html"
	context_object_name = "event"