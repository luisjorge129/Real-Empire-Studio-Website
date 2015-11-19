from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from rest_framework import generics

from .models import Event
from .serializers import EventListSerializer


class ApiEventList(generics.ListAPIView):
    queryset = Event.objects.filter(status=True)
    serializer_class = EventListSerializer


class EventsListView(ListView):
	queryset = Event.objects.filter(status=True)
	template_name = "events_list.html"
	context_object_name = "events"


class EventsDetailView(DetailView):
	queryset = Event.objects.filter(status=True)
	template_name = "events_detail.html"
	context_object_name = "event"