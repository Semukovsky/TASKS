from flask import Flask, request, url_for
import os

app = Flask(__name__)


upload_folder = os.path.join(app.root_path, 'static', 'img')
app.config['UPLOAD_FOLDER'] = upload_folder


@app.route('/load_photo', methods=['GET', 'POST'])
def run():
    if request.method == 'GET':
        return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="{url_for('static', filename='css/styles.css')}">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <title>program_4</title>
  </head>
  <body>
    <form class="login_form" method="post" enctype="multipart/form-data">
      <h1 class='text'>Загрузка фотографии</h1>
      <h2 class='text'>для участия в миссии</h2>
      <div class='main'>
        <div class="alert alert-primary" role="alert">
          <div class="form-group">
            <label for="photo">Приложите фотографию</label>
            <input type="file" class="form-control-file" id="photo" name="file">
          </div>
          <br>
          <img src="{url_for('static', filename='img/image.png')}" alt="здесь должна была быть картинка, но не нашлась" width="300">
          <br>
          <button type="submit" class="btn">Записаться</button>
        </div>
      </div>
    </form>
  </body>
</html>'''

    elif request.method == 'POST':
        photo = request.files['file']
        if photo:
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], 'image.png')
            photo.save(save_path)

        return f'''
        <!doctype html>
        <html>
          <head>
            <meta charset="utf-8">
            <title>Фото загружено</title>
          </head>
          <body>
            <h1>Фотография успешно загружена!</h1>
            <img src="{url_for('static', filename='img/image.png')}" alt="загруженное фото" width="350">
            <p><a href="{url_for('run')}">Загрузить другую</a></p>
          </body>
        </html>
        '''


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(port=8080, host='127.0.0.1')
