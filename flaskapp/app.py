from flask import Flask, render_template
import os
BASE_DIR = os.getcwd()
print(BASE_DIR)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/audiototext")
def audiototext():
    return render_template('audiototext.html')

# @app.route("/audiototext")
# def audiototext():
#     return render_template('audiototext.html')

# @app.route("/audiototext")
# def audiototext():
#     return render_template('audiototext.html')

# @app.route("/audiototext")
# def audiototext():
#     return render_template('audiototext.html')


# @app.route("/")
# def render()
# @app.route("/")
# def run_script():
#     file = open(f"{BASE_DIR}/main.py").read()
#     return exec(file)


@app.errorhandler(404)
def not_found(error):
    """Page not found."""
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
