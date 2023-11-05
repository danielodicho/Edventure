import requests

google_api_key = 'placeholder'

def get_location():
    """Get the geolocation information."""
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + google_api_key
    data = {'considerIp': 'true'}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json()['location']
    else:
        raise Exception('Error getting location:', response.text)
def get_city(lat, lng):
    """Convert the latitude and longitude to a city name."""
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={google_api_key}&result_type=locality"

    response = requests.get(geocode_url)

    if response.status_code == 200:
        results = response.json()['results']
        if results:
            for component in results[0]['address_components']:
                if "locality" in component['types']:
                    return component['long_name']
        raise Exception("No locality found for the location.")
    else:
        raise Exception('Error reverse geocoding:', response.text)
