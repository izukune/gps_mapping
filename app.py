from flask import Flask, render_template, request, logging, Response, redirect, flash, url_for, jsonify
from module import str2matrix, visualize_location

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/output", methods=['POST'])
def output():
    coord_list = request.form["coord_list"]
    print(coord_list)
    df = str2matrix(coord_list)
    return visualize_location(df)


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
