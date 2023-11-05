# Define the data structure
class HistoricalPOI:
    def __init__(self, name, description, category, coordinates):
        self.name = name
        self.description = description
        self.category = category
        self.coordinates = coordinates

# Create mock data
mock_pois = [
    HistoricalPOI("The Colosseum", "An oval amphitheatre in the centre of the city of Rome.", "Ancient", (41.8902, 12.4922)),
    # Add more POIs here...
]

# Selection logic
import random
def select_poi():
    return random.choice(mock_pois)

# API Endpoint
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_history_poi')
def get_history_poi():
    poi = select_poi()
    return jsonify(name=poi.name, description=poi.description, category=poi.category, coordinates=poi.coordinates)

if __name__ == '__main__':
    app.run(debug=True)
