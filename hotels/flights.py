import requests

from .hotels import get_access_token

LIST_OF_FLIGHTS_CRITERIA = "https://test.api.amadeus.com/v2/shopping/flight-offers"
SCHEDULE_FLIGHTS = "https://test.api.amadeus.com/v2/schedule/flights"
SEAT_MAPS = "https://test.api.amadeus.com/v1/analytics/itinerary-price-metrics"
FLIGHT_DESTINATION = "https://test.api.amadeus.com/v1/shopping/flight-destinations"
CHEAPEST_PRICE = "https://test.api.amadeus.com/v1/shopping/flight-dates"
TRAVEL_PREDICTIONS = "https://test.api.amadeus.com/v1/travel/predictions/flight-delay"
RECOMMENDED_LOCATIONS = "https://test.api.amadeus.com/v1/reference-data/recommended-locations"
PREDICTIONS_ON_TIME = "https://test.api.amadeus.com/v1/airport/predictions/on-time"
AIRPORT_LOCATIONS_BY_ID = "https://test.api.amadeus.com/v1/reference-data/locations/"
NEAREST_AIRPORT = "https://test.api.amadeus.com/v1/reference-data/locations/airports"
AIRPORT_ROUTES = "https://test.api.amadeus.com/v1/airport/direct-destinations"
CHECK_IN = "https://test.api.amadeus.com/v2/reference-data/urls/checkin-links"
AIRLINES_INFO = "https://test.api.amadeus.com/v1/reference-data/airlines"
AIRLINES_ROUTES = "https://test.api.amadeus.com/v1/airline/destinations"


def search_list_of_flights(originLocationCode,
                           destinationLocationCode,
                           departureDate,
                           adults):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "originLocationCode": originLocationCode,
        "destinationLocationCode": destinationLocationCode,
        "departureDate": departureDate,
        "adults": adults
    }
    resp = requests.get(LIST_OF_FLIGHTS_CRITERIA, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def get_itinerary_price_metrics(origin, destination, departure_date):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "originIataCode": origin,
        "destinationIataCode": destination,
        "departureDate": departure_date,
    }
    resp = requests.get(SEAT_MAPS, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def search_flight_destinations(params):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(FLIGHT_DESTINATION, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def cheap(origin, destination):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "origin": origin,
        "destination": destination
    }
    resp = requests.get(CHEAPEST_PRICE, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def recommended_locations(cityCodes):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "cityCodes": cityCodes,
    }
    resp = requests.get(RECOMMENDED_LOCATIONS, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def schedule_flights(params):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(SCHEDULE_FLIGHTS, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def travel_predictions(params):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(TRAVEL_PREDICTIONS, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def prediction_on_time(params):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(PREDICTIONS_ON_TIME, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def airport_locations(params):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(AIRPORT_LOCATIONS_BY_ID, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def airport_locations_by_id(locationId):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"{AIRPORT_LOCATIONS_BY_ID}/{locationId}", headers=headers)
    resp.raise_for_status()
    return resp.json()


def nearest_airport(params):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(NEAREST_AIRPORT, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def airport_routes(params):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(AIRPORT_ROUTES, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def airport_check_in(params):
    token = get_access_token()
    header = {"Authorization":f"Bearer {token}"}
    resp = requests.get(CHECK_IN,headers=header,params=params)
    resp.raise_for_status()
    return resp.json()


def airlines_info():
    token = get_access_token()
    headers= {"Authorization":f"Bearer {token}"}
    resp = requests.get(AIRLINES_INFO, headers=headers)
    resp.raise_for_status()
    return resp.json()


def airlines_routes(params):
    token = get_access_token()
    headers = {"Authorization":f"Bearer {token}"}
    resp = requests.get(AIRLINES_ROUTES,headers=headers,params=params)
    resp.raise_for_status()
    return resp.json()
