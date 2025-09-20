from .flights import *
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
            return Response({"error": "Should not be empty"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = list_hotels(keyword, subType)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class FlightsListView(APIView):
    def get(self, request):
        originLocationCode = request.query_params.get("originLocationCode")
        destinationLocationCode = request.query_params.get("destinationLocationCode")
        departureDate = request.query_params.get("departureDate")
        adults = request.query_params.get("adults")
        if not originLocationCode or not destinationLocationCode or not departureDate or not adults:
            return Response({"error": "Should not be empty"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = search_list_of_flights(originLocationCode, destinationLocationCode, departureDate, adults)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ItineraryPrice(APIView):
    def get(self, request):
        origin = request.query_params.get("originIataCode")
        destination = request.query_params.get("destinationIataCode")
        departure_date = request.query_params.get("departureDate")

        if not origin or not destination or not departure_date:
            return Response(
                {"error": "Should not be empty"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = get_itinerary_price_metrics(origin, destination, departure_date)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class FlightDestinations(APIView):
    def get(self, request):
        origin = request.query_params.get("origin")

        if not origin:
            return Response({"error": "origin is required (IATA code)"}, status=status.HTTP_400_BAD_REQUEST)

        params = {
            "origin": origin
        }

        try:
            data = search_flight_destinations(params)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class Cheap(APIView):
    def get(self, request):
        origin = request.query_params.get("origin")
        destination = request.query_params.get("destination")
        if not origin or not destination:
            return Response({"error": "Should not be empty"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = cheap(origin, destination)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class RecommendedLocations(APIView):
    def get(self, request):
        cityCodes = request.query_params.get("cityCodes")
        if not cityCodes:
            return Response({"error": "Should not be empty"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = recommended_locations(cityCodes)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ScheduleFlights(APIView):
    def get(self, request):
        carrierCode = request.query_params.get("carrierCode")
        flightNumber = request.query_params.get("flightNumber")
        scheduledDepartureDate = request.query_params.get("scheduledDepartureDate")

        if not carrierCode or not flightNumber or not scheduledDepartureDate:
            return Response({"error": "origin is required (IATA code)"}, status=status.HTTP_400_BAD_REQUEST)

        params = {
            "carrierCode": carrierCode,
            "flightNumber": flightNumber,
            "scheduledDepartureDate": scheduledDepartureDate,

        }

        try:
            data = schedule_flights(params)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TravelPredictions(APIView):
    def get(self, request):
        originLocationCode = request.query_params.get("originLocationCode")
        destinationLocationCode = request.query_params.get("destinationLocationCode")
        departureDate = request.query_params.get("departureDate")
        departureTime = request.query_params.get("departureTime")
        arrivalDate = request.query_params.get("arrivalDate")
        arrivalTime = request.query_params.get("arrivalTime")
        aircraftCode = request.query_params.get("aircraftCode")
        carrierCode = request.query_params.get("carrierCode")
        flightNumber = request.query_params.get("flightNumber")
        duration = request.query_params.get("duration ")

        if (not originLocationCode or not destinationLocationCode or not departureDate
                or not departureTime or not arrivalDate or not arrivalTime or not aircraftCode
                or not carrierCode or not flightNumber or not duration):
            return Response({"error": "Should not be empty"}, status=status.HTTP_400_BAD_REQUEST)

        params = {
            "originLocationCode": originLocationCode,
            "destinationLocationCode": destinationLocationCode,
            "departureDate": departureDate,
            "departureTime": departureTime,
            "arrivalDate": arrivalDate,
            "arrivalTime": arrivalTime,
            "aircraftCode": aircraftCode,
            "carrierCode": carrierCode,
            "flightNumber": flightNumber,
            "duration": duration,

        }

        try:
            data = travel_predictions(params)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PredictionOnTime(APIView):
    def get(self, request):
        airportCode = request.query_params.get("airportCode")
        date = request.query_params.get("date")

        if not airportCode or not date:
            return Response({"error": "Should not be empty"}, status=status.HTTP_400_BAD_REQUEST)

        params = {
            "airportCode": airportCode,
            "date": date,

        }

        try:
            data = prediction_on_time(params)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AirportLocations(APIView):
    def get(self, request, locationId=None):
        if locationId:
            try:
                data = airport_locations_by_id(locationId)
                if not data:
                    return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        subType = request.query_params.get("subType")
        keyword = request.query_params.get("keyword")
        if not subType or not keyword:
            return Response({"error": "Should not be empty"}, status=status.HTTP_400_BAD_REQUEST)

        params = {
            "subType": subType,
            "keyword": keyword
        }
        try:
            data = airport_locations(params)
            if not data:
                return Response({"error": "Not found "}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class NearestAirport(APIView):
    def get(self, request):
        latitude = request.query_params.get("latitude")
        longitude = request.query_params.get("longitude")
        if not latitude or not longitude:
            return Response({"error": "Should not be empty"}, status=status.HTTP_400_BAD_REQUEST)
        params = {
            "latitude": latitude,
            "longitude": longitude
        }
        try:
            data = nearest_airport(params)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AirportRoutes(APIView):
    def get(self, request):
        departureAirportCode = request.query_params.get("departureAirportCode")
        if not departureAirportCode:
            return Response({"error": "Should not be empty"}, status=status.HTTP_400_BAD_REQUEST)
        params = {
            "departureAirportCode": departureAirportCode,
        }
        try:
            data = airport_routes(params)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AirportCheckIn(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        airlineCode = request.query_params.get("airlineCode")
        if not airlineCode:
            return Response({"error":"Should not be empty"}, status=status.HTTP_400_BAD_REQUEST)

        params = {
            "airlineCode":airlineCode
        }

        try:
            data = airport_check_in(params)
            if not data:
                return Response({"error":"Not found "}, status=status.HTTP_404_NOT_FOUND)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AirlinesInfo(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        try:
            data = airlines_info()
            if not data:
                return Response({"error":"Data not found "}, status=status.HTTP_404_NOT_FOUND)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AirlinesRoutes(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        airlineCode = request.query_params.get("airlineCode")
        if not airlineCode:
            return Response({"error":"Should not be empty"}, status=status.HTTP_400_BAD_REQUEST)
        params ={
            "airlineCode":airlineCode
        }
        try:
            data = airlines_routes(params)
            if not data:
                return Response({"error":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)





