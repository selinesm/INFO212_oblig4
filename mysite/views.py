from flask import Blueprint, render_template
from models import Employee
from flask import Flask, request, jsonify

views = Blueprint("views", __name__)


# create view for the Home Page
@views.route("/")
def home():
    return render_template("home.html")






@staticmethod
def create(name, address, branch):
    return Employee(name, address, branch)
        
def read(self):
    return f"Name: {self.name}, address: {self.address}, branch: {self.branch}"

def update(self):
    pass

@staticmethod
def delete(employee):
    del employee