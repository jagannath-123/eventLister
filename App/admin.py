from django.contrib import admin

from App.models import Event, Admin

# Register your models here.
admin.site.register(Admin)
admin.site.register(Event)