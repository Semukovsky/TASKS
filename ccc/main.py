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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)