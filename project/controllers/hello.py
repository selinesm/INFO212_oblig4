from project import app
from flask import render_template, request, redirect, url_for
from project.models.User import findUserByUsername

#route index
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        data = {}
        try:
            user = findUserByUsername(username)
            data = {
                "username": user.username,
                "email": user.email
            }
        except:
            print ("error")

    else:
        data = {
            "username": "Not specified",
            "email": "Not specified"
        }
    
    return render_template('login.html', data = data)


