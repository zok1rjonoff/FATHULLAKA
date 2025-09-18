from django.shortcuts import render
from rest_framework import generics

from hotels.models import Users
from hotels.serializers import UsersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .hotels import *


class CitySearchView(APIView):
    def get(self, request):
        keyword = request.query_params.get("keyword")
        country_code = request.query_params.get("countryCode")
        try:
            data = search_city(keyword, country_code)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class HotelById(APIView):
    def get(self, request):
        hotel_ids = request.query_params.get("hotelIds")
        if not hotel_ids:
            return Response({"error": "Should not be empty"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = search_hotels(hotel_ids.split(','))
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class HotelInCityView(APIView):
    def get(self, request):
        cityCode = request.query_params.get("cityCode")
        if not cityCode:
            return Response({"error": "Should not be empty"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = search_hotels_in_city(cityCode)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class HotelsWithGeocode(APIView):
    def get(self, request):
        latitude = request.query_params.get("latitude")
        longitude = request.query_params.get("longitude")
        if not latitude or not longitude:
            return Response({"error": "Should not be empty"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = search_hotels_with_geocode(latitude, longitude)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class HotelSentiments(APIView):
    def get(self, request):
        hotelIds = request.query_params.get("hotelIds")
        if not hotelIds:
            return Response({"error": "Should not be empty"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = hotel_sentiments(hotelIds)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class HotelList(APIView):
    def get(self, request):
        keyword = request.query_params.get("keyword")
        subType = request.query_params.get("subType")
        if not keyword or not subType:
            return Response({"error":"Should not be empty"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = list_hotels(keyword,subType)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
class UserListCreateApiView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
