from flask import Flask, render_template
from register import RegisterForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "GEEKBRAINS GEEKBRAINS"

# @app.route("/")
# def index():
#     return "<h1>Hello, world!</h1>"


@app.route("/")  # декоратор - обработчик событий
def index():
    return render_template('index.html', title = 'Главная страница')



@app.route("/student", methods=["GET"])
def info():
    list_std = ['Саша', 'Masha', 'Petya', 'Robert', 'Alex']
    return render_template ('list_student.html', s = list_std, 
                            title = 'Online')

@app.route("/reg", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print(form.data)  # тип данных: dictionary
        print(form.data['name'], form.data['mail'])
    return render_template("register.html", form = form)



if __name__ == '__main__':
    app.run()