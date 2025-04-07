import json
import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/member')
def member():
    with open('templates/json.json', 'r', encoding='utf-8')  as file:
        dt = json.load(file)
        print(dt)
    return render_template('main.html', member=random.choice(dt))

@app.route('/index/<title>')

def index(title):
    return render_template('base.html', title=title)

if __name__ == '__main__':
    app.run('127.0.0.1', port=8080)