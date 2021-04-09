import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # checks if username already exists in database
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already in use")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Account created!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("sign_up.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if password matches with password in db
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Hello again, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # password does not match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("log_in"))

        else:
            # username not in db
            flash("Incorrect Username and/or Password")
            return redirect(url_for("log_in"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    spots = []
    if session["user"]:
        spots = list(mongo.db.spots.find({'created_by': username}))
        countries = list(mongo.db.countries.find().sort("country_name", 1))
        return render_template(
            "profile.html", username=username,
            countries=countries, spots=spots)

    return redirect(url_for("log_in"))


@app.route("/log_out")
def log_out():
    # remove user from session cookie
    flash("You are logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


@app.route("/spots")
def spots():
    spots = list(mongo.db.spots.find())
    return render_template("spots.html", spots=spots)


@app.route("/add_spot", methods=["GET", "POST"])
def add_spot():
    if request.method == "POST":
        spot = {
            "country_name": request.form.get("country_name"),
            "spot_name": request.form.get("spot_name"),
            "spot_region": request.form.get("spot_region"),
            "spot_level": request.form.get("spot_level"),
            "spot_best_time": request.form.get("spot_best_time"),
            "spot_description": request.form.get("task_description"),
            "spot_image": request.form.get("spot_image"),
            "spot_location": request.form.get("spot_location"),
            "created_by": session["user"]
        }
        mongo.db.spots.insert_one(spot)
        flash("Your spot has been successfully added!")
        return redirect(url_for("spots"))

    countries = list(mongo.db.countries.find().sort("country_name", 1))
    return render_template("add_spot.html", countries=countries)


@app.route("/edit_spot/<spot_id>", methods=["GET", "POST"])
def edit_spot(spot_id):
    if request.method == "POST":
        submit = {
                "country_name": request.form.get("country_name"),
                "spot_name": request.form.get("spot_name"),
                "spot_region": request.form.get("spot_region"),
                "spot_level": request.form.get("spot_level"),
                "spot_best_time": request.form.get("spot_best_time"),
                "spot_description": request.form.get("task_description"),
                "spot_image": request.form.get("spot_image"),
                "spot_location": request.form.get("spot_location"),
                "created_by": session["user"]
        }
        mongo.db.spots.update({"_id": ObjectId(spot_id)}, submit)
        flash("Spot successfully updated")

    spot = mongo.db.spots.find_one({"_id": ObjectId(spot_id)})
    countries = list(mongo.db.countries.find().sort("category_name", 1))
    return render_template("edit_spot.html", spot=spot, countries=countries)


@app.route("/delete_spot/<spot_id>")
def delete_spot(spot_id):
    mongo.db.spots.remove({"_id": ObjectId(spot_id)})
    flash("Spot Successfully Deleted")
    return redirect(url_for("spots"))


@app.route("/countries")
def countries():
    countries = list(mongo.db.countries.find().sort("country_name", 1))
    return render_template("countries.html", countries=countries)


@app.route("/add_country", methods=["GET", "POST"])
def add_country():
    if request.method == "POST":
        country = {
            "country_name": request.form.get("country_name"),
            "country_img": request.form.get("image_url")
        }
        mongo.db.countries.insert_one(country)
        flash("New Country Added")
        return redirect(url_for("countries"))

    return render_template("add_country.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
