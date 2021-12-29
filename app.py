
from flask import Flask, render_template, request
from yelp_api import *

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
    
    print(request.form.get("Food"))
    search_result()   

    return render_template("find.html")
