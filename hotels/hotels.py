import requests

CLIENT_ID = "9Rpw4rGQEfRwKuRVNdI15lxRCEOuWAsH"
CLIENT_SECRET = "NqYZbbQeoVzxjB2B"

AUTH_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
CITY_URL = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
HOTEL_URL = "https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-hotels"
HOTEL_IN_CITY_URL = "https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city"
HOTELS_WITH_GEOCODE = "https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-geocode"
HOTELS_SENTIMENTS = "https://test.api.amadeus.com/v1/e-reputation/hotel-sentiments"
HOTELS_BY_VALUES = "https://test.api.amadeus.com/v1/reference-data/locations/hotel"


def get_access_token():
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    resp = requests.post(AUTH_URL, data=data, headers=headers)
    resp.raise_for_status()
    token = resp.json()["access_token"]
    print(f"Token 1 {token}")
    return token


def search_city(keyword, country_code, max_results=10):
    token = get_access_token()
    print(f"Token 2 {token}")
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "countryCode": country_code,
        "keyword": keyword,
        "max": max_results,
        "include": "AIRPORTS",
    }
    resp = requests.get(CITY_URL, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def search_hotels(hotel_ids):
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"hotelIds": ",".join(hotel_ids)}
    resp = requests.get(HOTEL_URL, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def search_hotels_in_city(city_code):
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"cityCode": city_code}   # 🔹 bu joyda city_code dan foydalanamiz
    resp = requests.get(HOTEL_IN_CITY_URL, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def search_hotels_with_geocode(latitude, longitude):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "latitude":latitude,
        "longitude":longitude
    }
    resp = requests.get(HOTELS_WITH_GEOCODE,headers=headers,params=params)
    resp.raise_for_status()
    return resp.json()


def hotel_sentiments(hotelIds):
    token = get_access_token()

    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "hotelIds":hotelIds
    }
    resp = requests.get(HOTELS_SENTIMENTS, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def list_hotels(keyword, subType):
    token = get_access_token()
    headers = {"Authorization":f"Bearer {token}"}
    params = {
        "keyword":keyword,
        "subType":subType
    }
    resp = requests.get(HOTELS_BY_VALUES,headers=headers,params=params)
    resp.raise_for_status()
    return resp.json()