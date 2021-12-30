from flask import Flask, render_template, request

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
    print(request.form.get("Location"))
    print(request.form.get("suggested"))
    print(request.form.get("price"))
    #yelp_api.hello("hello") 

    return render_template("find.html")
