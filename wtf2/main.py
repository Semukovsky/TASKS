from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'geystvo'

@app.route('/training/<prof>')
def training(prof):
    prof_flag = False
    if prof.lower() == 'инженер' or prof.lower()== 'строитель':
        prof_flag =True
    return render_template('training.html', prof=prof_flag)

@app.route('/index/<title>')

def index(title):
    return render_template('base.html', title=title)

if __name__ == '__main__':
    app.run('127.0.0.1', port=8080)