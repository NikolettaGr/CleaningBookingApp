from django import forms
from .models import Booking
from django.utils import timezone


HOUSE = 'house'
APARTMENT = 'apartment'
VILLA = 'villa'

PROPERTY_CHOICES = (
    (HOUSE, 'House'),
    (APARTMENT, 'Apartment'),
    (VILLA, 'Villa'),
)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone_number',
        'date', 'time', 'property_type', 'kvm', 'notes']

    property_type = forms.MultipleChoiceField(
        choices=PROPERTY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True)

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Select a date',required=True
    )
    
    def clean_date(self):
        date = self.cleaned_data.get('date')
        current_time = timezone.now().date()
        
        if date < current_time:
            raise forms.ValidationError('Booking date must be in the future.')

        return date
