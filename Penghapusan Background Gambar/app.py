from flask import Flask, render_template, request, send_file, redirect, url_for
from rembg import remove
from PIL import Image
import os
import io
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
PROCESSED_FOLDER = "static/processed"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No file part"
    
    file = request.files['image']
    if file.filename == '':
        return "No selected file"
    
    # Mengamankan nama file
    filename = secure_filename(file.filename)
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    output_filename = "no_bg_" + filename
    output_path = os.path.join(PROCESSED_FOLDER, output_filename)
    
    # Simpan file asli
    file.save(input_path)
    
    # Proses remove background
    with open(input_path, "rb") as inp_file:
        input_image = inp_file.read()
        output_image = remove(input_image)  # RemBG bekerja dengan bytes
    
    # Simpan hasil sebagai PNG
    image = Image.open(io.BytesIO(output_image)).convert("RGBA")
    image.save(output_path, format="PNG")

    # Redirect ke halaman hasil dengan timestamp untuk mencegah caching
    return redirect(url_for('result', filename=output_filename, _t=int(os.path.getmtime(output_path))))

@app.route('/result')
def result():
    filename = request.args.get('filename')
    if not filename:
        return "File not found"
    return render_template('result.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
    path = os.path.join(PROCESSED_FOLDER, filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
