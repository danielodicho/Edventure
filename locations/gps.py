import requests

google_api_key = 'AIzaSyD2iA0S2ck8uFD-4NqplKRuku4XG7lEYkQ'

def get_location():
    """Get the geolocation information."""
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + google_api_key
    data = {'considerIp': 'true'}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json()['location']
    else:
        raise Exception('Error getting location:', response.text)


def get_places():
    """Get the places near the location."""
    user_location = get_location()
    latitude = user_location['lat']
    longitude = user_location['lng']
    user_location = f"{latitude},{longitude}"
    # user_location = '37.7749,-122.4194'
    print(user_location)
    keyword = ''

    # nature_types = ['park', 'campground', 'natural_feature']
    nature_types = []

    spots = []
    if nature_types:
        for place_type in nature_types:
            places_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={user_location}&radius=805&type={place_type}&key={google_api_key}"
            response = requests.get(places_url)
            places_data = response.json()

            # Append up to 10 spots of each type to the nature_spots list
            spots.extend(places_data['results'][:10])
    else:
        places_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={user_location}&radius=10000&key={google_api_key}"
        response = requests.get(places_url)
        places_data = response.json()
        spots = places_data['results'][:10]

    # Deduplicate spots based on place_id just in case
    unique_spots = {spot['place_id']: spot for spot in spots}.values()

    # Format these spots for the ChatGPT prompter
    formatted_spots = [f"{spot['name']} located at {spot['vicinity']}" for spot in unique_spots]
    return formatted_spots

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
