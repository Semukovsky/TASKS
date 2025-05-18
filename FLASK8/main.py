import os
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename:
            filename = file.filename.replace(" ", "_")
            path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path_to_save)
            return redirect(url_for('gallery'))

    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('gallery.html', images=images)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
