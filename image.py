from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Set the folder to store uploaded files
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']

    if file.filename == '':
        return 'No selected file'
    
    if file:
        # Save the file to the specified upload folder
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return 'File successfully uploaded!'

if __name__ == '__main__':
    # Ensure the upload folder exists
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)

