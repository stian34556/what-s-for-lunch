from flask import Flask, render_template, request
import yelp_api

app = Flask(__name__)

FOOD = [
    "American","Asian", "Barbecue","Chinese", "European",
    "Fast Food","French","Halal", "Italian", "Japanese",
    "Korean","Mexican","Vegetarian","Vietnamese"
]

@app.route("/login", methods = ["POST", "GET"])
def login():
    return render_template("login.html")

@app.route("/")
def home():
    return render_template("home.html", suggested=FOOD)

@app.route("/find", methods = ["POST"])
def find():
    
    term = request.form.get("suggested")
    location = request.form.get("Location")
    price = request.form.get("price")
    radius = request.form.get("radius")
    if (price == "$"):
        price = "1"
    elif (price == "$$"):
        price = "2"
    elif (price == "$$$"):
        price = "3"
    else:
        price = yelp_api.DEFAULT_PRICE
    radius = "10000"
    results = yelp_api.search_result(term, location, price, radius)
    print(results)

    return render_template("find.html", results = results)
