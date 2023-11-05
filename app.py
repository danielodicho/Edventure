from flask import Flask, request, jsonify, render_template
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    # Renders the index.html file
    return render_template('index.html')

if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    #app.run(host='0.0.0.0', port=5000)
    app.run(debug=False)
