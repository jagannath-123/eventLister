from rest_framework import serializers
from .models import Admin, Event

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'institute', 'password')



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'even_date', 'registration_last_date', 'duration', 'price', 'place', 'visits', 'link', 'admin' )