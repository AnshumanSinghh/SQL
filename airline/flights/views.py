from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flights, Passenger
# Create your views here.
def index(request):  
    return render(request, "flights/index.html", {
        "flights": Flights.objects.all()
    })


def flight(request, flight_id):
    flight = Flights.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight, 
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all(),
    })


def book(request, flight_id):  
    if request.method == "POST":
        # get the particular flight by its ID
        flight = Flights.objects.get(pk=flight_id)

        # get the particukar passenger which is equal to whatever was submitted via this POST form with a name of passenger.
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"])) # it menas that the data about which passenger ID we want to register on this flight is going
                                  # to be passed in via a form with an input field whose name is passenger[from any particular input field dictates
                                  # what name we get is received when a route like this book route is able to process the request from the user].
        
        passenger.flights.add(flight)  # to access passenger's flight(passenger.flights) and add new flight to it [.add(flight)].
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))