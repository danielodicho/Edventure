from flask import Flask, request, jsonify, render_template
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    # Renders the index.html file
    return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_image():
#     data = request.get_json()
#     if not data or 'image' not in data:
#         return jsonify({'error': 'No image data'}), 400

#     # Decode the image data
#     image_data = data['image']
#     image_data = image_data.replace('data:image/png;base64,', '')  # Remove the prefix
#     image_bytes = base64.b64decode(image_data)
    
#     # Convert bytes to a PIL Image
#     image = Image.open(BytesIO(image_bytes))

#     # TODO: Process the image here

#     return jsonify({'result': 'Image processed successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
