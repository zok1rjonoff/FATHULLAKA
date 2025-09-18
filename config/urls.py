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
from django.urls import path

from hotels.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserListCreateApiView.as_view(), name="user-list-create"),
    path("amadeus/cities", CitySearchView.as_view(), name="amadeus-cities"),
    path("amadeus/hotels", HotelById.as_view(), name="amadeus-hotels"),
    path("amadeus/hotels-in-city", HotelInCityView.as_view(), name="amadeus-hotels-in-city"),
    path("amadeus/hotels-with-geocode", HotelsWithGeocode.as_view(), name="amadeus-hotels-with-geocode"),
    path("amadeus/hotels-sentiments", HotelSentiments.as_view(), name="amadeus-hotels-sentiments"),
    path("amadeus/hotels-list", HotelList.as_view(), name="amadeus-hotels-list"),
]

