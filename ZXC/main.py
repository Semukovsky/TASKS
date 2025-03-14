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
    <h1>Жди нас, Марс!</h1>
    <br><img src="{url_for('static', filename='images/img.png')}" 
               alt="здесь должна была быть картинка, но не нашлась">
    <br><p>Вот она, красная планета</p>'''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
