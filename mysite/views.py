from flask import Blueprint, render_template, redirect
from models import Employee
from flask import Flask, request, jsonify

views = Blueprint("views", __name__)


# create view for the Home Page
@views.route("/")
def home():
    return render_template("home.html")


@views.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        branch = request.form['branch']
        employee = Employee(name=name, address=address, branch = branch)
        return redirect('/data')