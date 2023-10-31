
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, Flask
#from project import app
from models.my_dao import *
from user import *
#from models import Employee
from neo4j import GraphDatabase

app = Blueprint("views", __name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/", methods=["POST"])
def process_input():
    username = request.form.get("username_id")
    user, user_name, user_email = findUserByUsername(username)
    return render_template("home.html", username=user_name, useremail=user_email)



@app.route("/get_cars", methods=["GET"])
def query_records():
    return findAllCars()

# The method uses the registration number to find the car
# object from database
@app.route('/get_cars_by_reg_number', methods=['POST'])
def find_car_by_reg_number():
    record = json.loads(request.data)
    print(record)
    print(record['reg'])
    return findCarByReg(record['reg'])

@app.route('/save_car', methods=["POST"])
def save_car_info():
    record = json.loads(request.data)
    print(record)
    return save_car(
        record['make'], record['model'], record['reg'],
        record['year'], record['capacity'])

@app.route('/update_car', methods=['PUT'])
def update_car_info():
    record = json.loads(request.data)
    print(record)
    return update_car(
        record['make'], record['model'], record['reg'],
        record['year'], record['capacity'])

# The method uses the registration number to find the car
# object from database and removes the records
@app.route('/delete_car', methods=['DELETE'])
def delete_car_info():
    record = json.loads(request.data)
    print(record)
    delete_car(record['reg'])
    return findAllCars()


#EMPLOYEE

# Set up the Neo4j connection
"""""graph = GraphDatabase("bolt://localhost:7687", auth=("username", "password"))  # Replace with your Neo4j credentials

# Create (Add) a new employee
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    new_employee = Employee(name=data['name'], address=data['address'], branch=data['branch'])
    graph.create(new_employee)
    return jsonify(new_employee), 201

# Read (Get) employees
@app.route('/employees', methods=['GET'])
def get_employees():
    query = "MATCH (employee:Employee) RETURN employee"
    results = graph.run(query)
    employee_data = [record['employee'] for record in results]
    return jsonify(employee_data)

# Update (Edit) employee information
@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.json
    query = "MATCH (employee:Employee) WHERE ID(employee) = $id SET employee.name = $name, employee.address = $address, employee.branch = $branch"
    graph.run(query, id=employee_id, name=data['name'], address=data['address'], branch=data['branch'])
    return 'Employee updated', 200

# Delete (Remove) an employee
@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    query = "MATCH (employee:Employee) WHERE ID(employee) = $id DELETE employee"
    graph.run(query, id=employee_id)
    return 'Employee deleted', 200"""""




