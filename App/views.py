from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AdminSerializer, EventSerializer
from .models import Admin, Event
# Create your views here.

class AdminView(viewsets.ModelViewSet):
    serializer_class = AdminSerializer
    queryset = Admin.objects.all()


class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()