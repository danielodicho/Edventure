from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask import Flask, request, jsonify, render_template, jsonify
from io import BytesIO
from PIL import Image
import base64
import os

#setting up the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///edventure.db'
app.config['SECRET_KEY'] = 'mysecretkey' # placeholder for now
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

admin = Admin(app, name='Edventure Admin', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))


@app.route('/')
def index():
    # new_user = User(username='flask', email='example@example.com')
    # db.session.add(new_user)
    # db.session.commit()
#     return 'Hi!'



    # Renders the index.html file
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    data = request.get_json()
    if not data or 'image' not in data:
        return jsonify({'error': 'No image data'}), 400

    # Decode the image data
    image_data = data['image']
    image_data = image_data.replace('data:image/png;base64,', '')  # Remove the prefix
    image_bytes = base64.b64decode(image_data)
    
    # Convert bytes to a PIL Image
    image = Image.open(BytesIO(image_bytes))

    # TODO: Process the image here

    return jsonify({'result': 'Image processed successfully'}), 200


@app.route('/save-image', methods=['POST'])
def save_image():
    data = request.json['image']
    # Remove the header from the data URL
    header, encoded = data.split(",", 1)
    # Decode the base64 string
    data = base64.b64decode(encoded)

    # Create an image from the bytes and save it
    with Image.open(BytesIO(data)) as img:
        # Specify the directory and filename to save the image
        file_path = os.path.join('opencv', 'captured_image.png')
        img.save(file_path, 'PNG')

    return jsonify({'message': 'Image saved successfully'}), 200

# Create the database and tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=False)
