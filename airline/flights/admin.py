from django.contrib import admin

from .models import Flights, Airport, Passenger

# Register your models here.

# create a class called FlightAdmin which is going to be subclass of ModelAdmin
class FlightAdmin(admin.ModelAdmin): # to customize our admin page it will show all the details mentioned here on our admin page.
    list_display = ("id", "origin", "destination", "duration")

# By this when we are editing a passenger, we can have a special way of manipulating many to many relationships inside of an attribute
# called filter_horizontal, if I use this on flights this will just make it a little bit micer for manipulating the flights that a passenger is on.
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flights, FlightAdmin) # we have customize our admin page for Flights so we have to include it here 
admin.site.register(Passenger, PassengerAdmin)
