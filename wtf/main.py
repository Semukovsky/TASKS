from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zxc'


@app.route('/index')
def index():
    title = request.args.get('title', 'casebatle')
    return render_template('base.html', title=title)


if __name__ == '__main__':
    app.run('127.0.0.1', port=8080)