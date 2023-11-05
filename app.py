from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask import Flask, request, render_template, jsonify, Response
from io import BytesIO
from PIL import Image
import base64
import os
import cv2
import numpy as np



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
# Load the model
net = cv2.dnn.readNetFromCaffe('/Users/neelshettigar/Downloads/Edventure/opencv/deploy.prototxt', '/Users/neelshettigar/Downloads/Edventure/opencv/mobilenet_iter_73000.caffemodel')

# Define the class labels MobileNet SSD was trained on
classNames = {
    0: 'background', 1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
    5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
    10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse',
    14: 'motorbike', 15: 'person', 16: 'pottedplant',
    17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor'
}

def gen_frames():
    # Initialize video feed from webcam
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
            net.setInput(blob)
            detections = net.forward()

            # Loop over the detections
            for i in range(detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > 0.2:
                    class_id = int(detections[0, 0, i, 1])
                    class_name = classNames[class_id]
                    box_x = int(detections[0, 0, i, 3] * frame.shape[1])
                    box_y = int(detections[0, 0, i, 4] * frame.shape[0])
                    box_width = int(detections[0, 0, i, 5] * frame.shape[1])
                    box_height = int(detections[0, 0, i, 6] * frame.shape[0])
                    cv2.rectangle(frame, (box_x, box_y), (box_width, box_height), (23, 230, 210), thickness=2)
                    cv2.putText(frame, class_name, (box_x, box_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (23, 230, 210), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Concatenate frame one by one and show result

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


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
