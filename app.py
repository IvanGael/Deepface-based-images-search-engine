import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from deepface import DeepFace
from database import get_all_images
from init_db import initialize_database

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Find similar faces
            similar_images = find_similar_faces(filepath)
            
            return jsonify({'similar_images': similar_images})
    
    return render_template('index.html')

def find_similar_faces(uploaded_image):
    all_images = get_all_images()
    similar_images = []
    
    for db_image in all_images:
        try:
            result = DeepFace.verify(img1_path=uploaded_image, img2_path=db_image['path'])
            print(f'result {result}')
            if result['verified']:
                similar_images.append(db_image['path'])
        except:
            pass
    
    return similar_images

if __name__ == '__main__':
    # Initialize the database (this will only happen once)
    initialize_database()
    app.run(debug=True)