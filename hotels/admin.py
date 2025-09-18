from django.contrib import admin
from .models import Users, Flight, Hotel, Car, Tour, Booking


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone_number", "bonus_points", "preferred_language", "is_active", "is_staff")
    search_fields = ("username", "email", "phone_number")
    list_filter = ("preferred_language", "is_active", "is_staff")


@admin.register(Flight)
class FlightsAdmin(admin.ModelAdmin):
    list_display = ("airline", "flight_number", "departure", "arrival", "aircraft_type", "price", "available_seats")
    search_fields = ("airline", "flight_number", "aircraft_type")
    list_filter = ("airline", "departure", "arrival")


@admin.register(Hotel)
class HotelsAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "country", "rating", "price_range", "availability")
    search_fields = ("name", "city", "country")
    list_filter = ("city", "country", "availability")


@admin.register(Car)
class CarsAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "year", "transmission", "price_per_day", "location", "availability")
    search_fields = ("brand", "model", "location")
    list_filter = ("brand", "year", "availability")


@admin.register(Tour)
class ToursAdmin(admin.ModelAdmin):
    list_display = ("title", "duration", "price", "schedule")
    search_fields = ("title", "description")
    list_filter = ("schedule",)


@admin.register(Booking)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ("user", "service_type", "service_id", "status", "total_price", "booking_date", "payment_status")
    search_fields = ("user__username", "service_type", "status", "payment_status")
    list_filter = ("status", "payment_status", "booking_date")
