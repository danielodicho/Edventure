from gpt import *

try:
    # Get the geolocation
    location = get_location()
    lat, lng = location['lat'], location['lng']

    # Get the city name from the geolocation
    city = get_city(lat, lng)
    # Get cool things to do in the city from OpenAI's GPT
    context = "You are a road trip assistant for a driver who loves adventure and exploring"
    prompt = f"What are some fun and interesting places near {city}"

    places = get_response(context, prompt)
    print(places)

except Exception as e:
    print(e)
