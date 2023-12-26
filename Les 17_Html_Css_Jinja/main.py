from flask import Flask, render_template


app = Flask(__name__)

# @app.route("/")
# def index():
#     return "<h1>Hello, world!</h1>"


@app.route("/")
def index():
    return render_template('index.html', title = 'Главная страница')



@app.route("/student")
def info():
    list_std = ['Саша', 'Masha', 'Petya', 'Robert', 'Alex']
    return render_template ('list_student.html', s = list_std, 
                            title = 'Online')



if __name__ == '__main__':
    app.run()