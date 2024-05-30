from flask import Flask, request, render_template
import os
from vision_plugin import VisionPlugin

app = Flask(__name__)

# Configure the path for uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize the vision plugin
vision_plugin = VisionPlugin()

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods=['POST'])
def upload_file_post():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        # Process the file with the vision plugin
        image_view = vision_plugin.process_image(filename)
        return render_template('view_image.html', image_view=image_view)

if __name__ == '__main__':
    app.run(debug=True)
