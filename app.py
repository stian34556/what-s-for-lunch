from flask import Flask, render_template, request, redirect, url_for, flash
import yelp_api
import random

app = Flask(__name__)
app.secret_key = "hello"

login = False

FOOD = [
    "American","Asian", "Barbecue","Chinese", "European",
    "Fast Food","French","Halal", "Italian", "Japanese",
    "Korean","Mexican","Vegetarian","Vietnamese"
]

@app.route("/login.html", methods = ["POST", "GET"])
def login():
    return render_template("login.html")

@app.route('/welcome.html', methods=['GET', 'POST'])
def welcome():
    return render_template("welcome.html")

@app.route("/")
def home():
    return render_template("home.html", suggested=FOOD)

@app.route("/index")
def index():
    return render_template("index.html")    

@app.route("/find", methods = ["POST"])
def find():
    
    term = request.form.get("suggested")
    term += "+ food"

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
     
    results = yelp_api.search_result(term, location, price, radius)

    random_price = str(random.randint(1, 3))
    rec = yelp_api.search_result("food", location, random_price, radius)
    random_price = int(random_price)

    if (results == "none"):
        flash('none')
        return redirect(url_for('home'))

    else:
        return render_template("find.html", results = results, rec = rec, random_price = random_price)