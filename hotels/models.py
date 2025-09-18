from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    phone_number = models.CharField(max_length=15)
    bonus_points = models.PositiveIntegerField(default=0)
    preferred_language = models.CharField(max_length=5)


class Flight(models.Model):
    airline = models.CharField(max_length=150)
    flight_number = models.CharField(max_length=60)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    aircraft_type = models.CharField(max_length=160)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()


class Hotel(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    amenities = models.CharField(max_length=255)
    photos = models.FileField(upload_to='hotels')
    price_range = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)


class Car(models.Model):
    model = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    year = models.PositiveIntegerField()
    transmission = models.CharField(max_length=150)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=250)
    availability = models.BooleanField(default=True)


class Tour(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in days")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inclusions = models.CharField(max_length=255)
    schedule = models.DateTimeField()


class Booking(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50)
    service_id = models.PositiveIntegerField()
    status = models.CharField(max_length=20, default="pending")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, default="unpaid")


class Payments(models.Model):
    pass

