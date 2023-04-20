from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "Hi<br><a href='/index'>go next</a>"

@app.route('/index/<x>/<y>')
def index(x,y):
    return f'Summa: {int(x) + int(y)}'

if __name__ == '__main__':
    app.run()