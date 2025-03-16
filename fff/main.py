from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def heads_1():
    return """
    <h1>Миссия Колонизация Марса</h1>
    """


@app.route('/index')
def index():
    return f'''<h1>И на Марсе будут яблони цвести!'''


@app.route('/promotion')
def promotion():
    return f'''<h1>Человечество вырастает из детства.
                <br>Человечеству мала одна планета.
                <br>Мы сделаем обитаемыми безжизненные пока планеты.
                <br>И начнем с Марса!
                <br>Присоединяйся!'''


@app.route('/image_mars')
def image():
    return f'''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Привет, Марс!</title>
    </head>
    <body>
    <h1>Жди нас, Марс!</h1>
    <br><img src="{url_for('static', filename='img/img.png')}" 
               alt="здесь должна была быть картинка, но не нашлась">
    <br><p>Вот она, красная планета</p>
    </body>
    </html>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.2.1/dist/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous"> 
            <link href="{url_for('static', filename='css/style.css')}" rel=stylesheet>
            <meta charset="UTF-8">
            <title>Привет, Марс!</title>
        </head>
        <body>
        <h1 class="title">Жди нас, Марс!</h1>
        <br><img src="{url_for('static', filename='img/img.png')}" 
                   alt="здесь должна была быть картинка, но не нашлась">
        <div class="alert alert-dark" role="alert">
            Человечество вырастает из детства.
        </div>
        <div class="alert alert-success" role="alert">
            Человечеству мала одна планета.
        </div>
        <div class="alert alert-secondary" role="alert">
            Мы сделаем обитаемыми безжизненные пока планеты.
        </div>
        <div class="alert alert-warning" role="alert">
            И начнем с Марса!
        </div>
        <div class="alert alert-danger" role="alert">
            Присоединяйся!
        </div>
        </body>
        </html>
        '''

@app.route('/carousel')
def carousel():
    return f'''<!DOCTYPE HTML>
            <head>
            <meta charset="utf-8">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='style.css')}">
            </head>
            <body>
            <h1>Пейзажи марса</h1>
            <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="{url_for('static', filename='img/img.png')}" height="800" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img src="{url_for('static', filename='img/img_1.png')}" height="800" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img src="{url_for('static', filename='img/img_2.png')}" height="800" class="d-block w-100" alt="...">
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
                    integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
                    crossorigin="anonymous"></script>
            </body>
            </html>'''


if __name__ == '__main__':
    app.run('127.0.0.1', port=8080)