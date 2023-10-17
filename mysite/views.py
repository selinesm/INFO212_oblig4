from flask import Blueprint, render_template

views = Blueprint("views", __name__)


# create view for the Home Page
@views.route("/")
def home():
    return render_template("home.html")