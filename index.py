from flask import render_template, request, redirect, flash, url_for
import urllib.request
from werkzeug.utils import secure_filename
from app import app
from new import predict
import os

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET','POST'])

def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            predict(filename)
            label = predict(filename)
            flash(label)
            flash(filename)
            return redirect('/')


if __name__ == "__main__":
    app.run()