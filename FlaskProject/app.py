from flask import Flask, render_template, redirect, url_for, request
from DB_handler import DBModule

app = Flask(__name__)
DB = DBModule()


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/list")
def post_list():
    pass


@app.route("/post/<int:pid>")
def post(pid):
    pass


@app.route("/login")
def login():
    pass


@app.route("/login_done")
def login_done():
    pass


@app.route("/signin")
def sign_in():
    return render_template("signin.html")


@app.route("/signin_done")
def signin_done():
    pass


@app.route("/user/<uid>")
def user():
    pass


@app.route("/write")
def write_post():
    pass


@app.route("/write_done", methods=["GET"])
def write_done():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
