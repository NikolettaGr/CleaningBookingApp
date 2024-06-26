from django.db import models


HOUSE = 'house'
APARTMENT = 'apartment'
VILLA = 'villa'

PROPERTY_CHOICES = (
    (HOUSE, 'House'),
    (APARTMENT, 'Apartment'),
    (VILLA, 'Villa'),
)


TIME_PERIODS = (
    (1, '07:00'),
    (2, '08:00'),
    (3, '09:00'),
    (4, '10:00'),
    (5, '11:00'),
    (6, '12:00'),
    (7, '13:00'),
    (8, '14:00'),
    (9, '15:00'),
)


class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(null=True, blank=True, max_length=15)
    date = models.DateField()
    time = models.IntegerField(choices=TIME_PERIODS, default=0)
    property_type = models.CharField(max_length=50, choices=PROPERTY_CHOICES)
    kvm = models.CharField(max_length=50)
    notes = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.date}'

