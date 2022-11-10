import scripts
from flask import Flask, render_template, redirect, request, url_for, flash
import os
import sys
from pprint import pprint
pprint(sys.path)
print("parentdirectory--->", os.pardir)
print("syspath", sys.path[0])
# PROJECT_ROOT = os.path.abspath(os.path.join(
#     os.path.dirname(__file__), '..'))
# print(PROJECT_ROOT)
# sys.path.append(PROJECT_ROOT)
# print(sys.path[0])

# tst = scripts.textStemmingTool()

print("script running---->", scripts.do_calculation(2, 3))

BASE_DIR = os.getcwd()
print(BASE_DIR)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/audiototext/", methods=["POST", "GET"])
def audiototext():
    if request.method == "POST":
        try:
            fname = request.form["fname"]
            formats = request.form["formats"]
            result = f"{fname}.{formats}"
            result = scripts.audioToText(fname, formats)
            return render_template('audiototext.html', filename=fname, format=formats, result=result)
        except:
            return render_template("404.html")
    return render_template('audiototext.html')


@app.route("/textstemmer/", methods=["POST", "GET"])
def textstemmer():
    if request.method == "POST":
        try:
            fname = request.form["fname"]
            formats = request.form["formats"]
            result = f"{fname}.{formats}"
            result = scripts.textStemming(fname, formats)
            return render_template('textstemmer.html', filename=fname, format=formats, result=result)
        except:
            return render_template("404.html")
    return render_template('textstemmer.html')


@app.route("/sentimentanalysis/", methods=["POST", "GET"])
def sentimentanalysis():
    if request.method == "POST":
        try:
            fname = request.form["fname"]
            formats = request.form["formats"]
            result = f"{fname}.{formats}"
            result = scripts.sentimentAnalysis(fname, formats)
            return render_template('sentimentanalysis.html', filename=fname, format=formats, result=result)
        except Exception as e:
            print("Error!!!!", e)
            return render_template("404.html")
    return render_template('sentimentanalysis.html')

# @app.route("/entityextraction/", methods=["POST", "GET"])
# def entityextraction():
#     if request.method == "POST":
#         try:
#             fname = request.form["fname"]
#             formats = request.form["formats"]
#             result = f"{fname}.{formats}"
#             result = scripts.entityextraction(fname, formats)
#             return render_template('entityextraction.html', filename=fname, format=formats, result=result)
#         except Exception as e:
#             print("Error!!!!", e)
#             return render_template("404.html")
#     return render_template('entityextraction.html')

# @app.route("/audiostemmer")
# def audiostemmer():
#     return render_template('audiostemmer.html')


# @app.route("/textstemmer")
# def textstemmer():
#     return render_template('textstemmer.html')


# @app.route("/audiototextscript")
# def runscript():
#     print("--------------------------------Inside script------------------------------------")
#     print(scripts.do_calculation(2, 3))

# -----------------------------------------------------------------
    # file = open(f"{BASE_DIR}/main.py", 'r').read()
    # print("Script opened...")
    # return exec(file)

# @app.route("/")
# def render()
# @app.route("/")
# def run_script():
#     file = open(f"{BASE_DIR}/main.py").read()
#     return exec(file)
# -----------------------------------------------------------------


@app.errorhandler(404)
def not_found(error):
    """Page not found."""
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
