from flask import Flask, render_template, request, redirect, url_for, flash
from detection import detect_animals
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'wildlife_conservation_secret'  # For session security

# Ensure 'uploads' folder exists for uploaded files
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Detection route
@app.route('/detect', methods=['POST'])
def detect():
    if 'file' not in request.files:
        flash('No file selected. Please upload an image or video.')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No file selected. Please choose a valid file.')
        return redirect(request.url)
    
    if file:
        # Save uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Perform detection
        output_path = detect_animals(file_path)

        if output_path:
            return render_template('results.html', result_image=output_path)
        else:
            flash('Detection failed. Please try again.')
            return redirect(request.url)

# Error handling
@app.errorhandler(404)
def not_found(e):
    return render_template('error.html'), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
