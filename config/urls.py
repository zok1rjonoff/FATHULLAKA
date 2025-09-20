"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from hotels.views import *

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("amadeus/cities", CitySearchView.as_view(), name="amadeus-cities"),
    path("amadeus/hotels", HotelById.as_view(), name="amadeus-hotels"),
    path("amadeus/hotels-in-city", HotelInCityView.as_view(), name="amadeus-hotels-in-city"),
    path("amadeus/hotels-with-geocode", HotelsWithGeocode.as_view(), name="amadeus-hotels-with-geocode"),
    path("amadeus/hotels-sentiments", HotelSentiments.as_view(), name="amadeus-hotels-sentiments"),
    path("amadeus/hotels-list", HotelList.as_view(), name="amadeus-hotels-list"),
    path("amadeus/flights-list", FlightsListView.as_view(), name="amadeus-flights-list"),
    path("amadeus/itinerary-price-metrics", ItineraryPrice.as_view(), name="amadeus-flights-seats"),
    path("amadeus/flight-destinations", FlightDestinations.as_view(), name="amadeus-flight-destinations"),
    path("amadeus/flight-cheap", Cheap.as_view(), name="amadeus-flight-cheap"),
    path("amadeus/flight-recommended-locations", RecommendedLocations.as_view(), name="amadeus-flight-recommended"),
    path("amadeus/flight-schedule-flights", ScheduleFlights.as_view(), name="amadeus-flight-schedule-flights"),
    path("amadeus/flight-travel-predictions", TravelPredictions.as_view(), name="amadeus-flight-travel-predictions"),
    path("amadeus/flight-travel-prediction-on-time", PredictionOnTime.as_view(), name="amadeus-flight-prediction-on-time"),
    path("amadeus/flight-airport-locations", AirportLocations.as_view(), name="amadeus-flight-airport-locations"),
    path("amadeus/flight-airport-location/<str:locationId>/", AirportLocations.as_view(), name="amadeus-flight-airport-location-by-id"),
    path("amadeus/flight-nearest-airport", NearestAirport.as_view(), name="amadeus-flight-nearest-airport"),
    path("amadeus/flight-airport-routes", AirportRoutes.as_view(), name="amadeus-flight-airport-routes"),
    path("amadeus/flight-airport-check-in", AirportCheckIn.as_view(), name="amadeus-flight-airport-check-in"),
    path("amadeus/airlines-info", AirlinesInfo.as_view(), name="amadeus-airlines-info"),
    path("amadeus/airlines-routes", AirlinesRoutes.as_view(), name="amadeus-airlines-routes"),

]

