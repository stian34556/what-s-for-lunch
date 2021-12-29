from flask import Flask, render_template, request

app = Flask(__name__)

FOOD = [
    "American",
    "Asian",
    "Barbecue",
    "Canadian",
    "Chinese",
    "Europen",
    "Fast Food",
    "French",
    "Halal",
    "Italian",
    "Japanese",
    "Korean",
    "Mexican",
    "Vegetarian",
    "Vietnamese"
]


@app.route("/login", methods = ["POST", "GET"])
def login():
    return render_template("login.html")


@app.route("/")
def home():
    return render_template("home.html", suggested=FOOD)

