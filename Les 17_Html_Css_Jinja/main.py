from flask import Flask, render_template


app = Flask(__name__)

# @app.route("/")
# def index():
#     return "<h1>Hello, world!</h1>"


@app.route("/")
def index():
    return render_template('index.html')



@app.route("/info")
def info():
    return "<h1>GEEKBRAINS</h1>"



if __name__ == '__main__':
    app.run()