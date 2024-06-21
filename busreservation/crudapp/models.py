from django.db import models

# Create your models here.
#from django.db import models
from django.db import models

class Reservation(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    departure_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    date_of_journey = models.DateField()
    time_of_departure = models.TimeField()
    number_of_seats = models.IntegerField()
    delete_flag = models.BooleanField(default=False)
    seat_preference = models.CharField(max_length=10, choices=[('window', 'Window'), ('aisle', 'Aisle'), ('any', 'Any')])


    def __str__(self):
        return self.full_name