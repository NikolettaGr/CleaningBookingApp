from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email',
                    'date', 'time',
                    'property_type', 'phone_number',
                    'notes')
    search_fields = ('full_name',
                     'date', 'time',
                     'phone_number')
    list_filter = ('full_name',
                   'date', 'time', 'property_type',
                   'phone_number')
