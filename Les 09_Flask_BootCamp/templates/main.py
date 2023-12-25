from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/info")
def info():
    return "<h1>GEEKBRAINS</h1>"


if __name___ == '__main__':
    app.run()