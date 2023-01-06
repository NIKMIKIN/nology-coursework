from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def main_page():
    return "Main Page"

@app.route("/page2")
def page2():
    return "Page 2"

@app.route("/random")
def html_random():
    return render_template("random.html")

# @app.route("/")
# def hello_monty():
#     return "Hello Monty!"

# #NEW ROUTE
# @app.route("/new")
# def hello_new():
#     return "Hellow NEW route!"

# #You can also handle logic within your route function
# @app.route("/math")
# def handle_math():
#     equation = 15 * 25 + 150 - 23 / 18
#     return str(equation)

# @app.route("/fancy")
# def html_world():
#     return render_template("fancy.html")