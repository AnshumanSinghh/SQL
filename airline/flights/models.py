from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flights(models.Model):
    # origin [will be ForeignKey] will take reference from Airport table
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

# to create databse, it is a two step process:
# 1. Cretae a migration & say here are the changes that i would 
# like to apply on databases. COMMAND: [python manage.py makemigrations], it will create model Flight(Table_name) inside migrations directory.

# 2. To apply these migrations, I will migrate those changes to tell Django to tale those changes & actually apply them
# to the databases. COMMAND: [python manage.py migrate], it will apply all the migrations including bunch of default migrations too.

    def __str__(self): # for string represenation of our table
        return f"{self.id}: {self.origin} to {self.destination} in {self.duration} minutes."

class Passenger(models.Model):
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flights, blank=True, related_name="passengers")  # to tell that passenger and Flights has many to many relation
    
    def __str__(self):
        return f"{self.fname} {self.lname}"
