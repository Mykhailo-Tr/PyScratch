from flask import Flask, redirect, request, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user")
def user():
    return "Hello, User!"

if __name__ == '__main__':
    app.run(debug=True, port=5555)