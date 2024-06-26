# Generated by Django 4.2.13 on 2024-06-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('date', models.DateField()),
                ('time', models.IntegerField(choices=[(1, '07:00'), (2, '08:00'), (3, '09:00'), (4, '10:00'), (5, '11:00'), (6, '12:00'), (7, '13:00'), (8, '14:00'), (9, '15:00')], default=0)),
                ('property_type', models.CharField(choices=[('house', 'House'), ('apartment', 'Apartment'), ('villa', 'Villa')], max_length=50)),
                ('kvm', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
