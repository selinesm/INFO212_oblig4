
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, Flask
from project.models.my_dao import *
from project.models.User import *
from neo4j import GraphDatabase
from project import app

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/", methods=["POST"])
def process_input():
    error_message = None
    username = request.form.get("username_id")
    user_info = findUserByUsername(username)

    try:
        if user_info:
            print(user_info)
            return redirect(url_for("app.home", username=user_info[0], useremail=user_info[1]))
        else:
            error_message = "Invalid account"
    except Exception as e:
        error_message = f"Error: {str(e)}"

    return render_template("login.html", error_message=error_message)


"""@app.route("/<username><useremail>")
def home(username, useremail):
    return render_template("home.html", username=username, useremail=useremail)"""


@app.route("/get_cars", methods=["GET"])
def query_records():
    return findAllCars()

# The method uses the registration number to find the car
# object from database
@app.route('/get_cars_by_reg_number', methods=['POST'])
def find_car_by_reg_number():
    try:
        record = request.get_json()  # Parse JSON data from the request body
        print(record)
        print(record['reg'])
        return jsonify(findCarByReg(record['reg']))
    except Exception as e:
        return jsonify({"error": "Invalid JSON data or missing 'reg' field"}), 400


@app.route('/save_car', methods=["POST"])
def save_car_info():
    record = json.loads(request.data)
    print(record)
    return save_car(
        record['make'], record['model'], record['reg'], record['year'],
        record['capacity'], record['id'], record['status'])

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

#Check if user has rented a car
def check_user(user_id):
    query = """
    MATCH (u:User {id: $user_id})-[:HAS_RENTED]->(c:Car)
    RETURN COUNT(c) > 0 AS has_rented
    """
    with GraphDatabase.driver(uri, auth=(user, password)) as driver:
        with driver.session() as session:
            result = session.run(query, user_id=user_id).single()
            if result:
                has_rented = result["has_rented"]
                return has_rented
            else:
                return False

@app.route('/check_user/<int:user_id>')
def check_rental_status(user_id):
    has_rented = check_user(user_id)
    
    if has_rented:
        return 'User has rented a car'
    else:
        return 'User has not rented a car'

#if __name__ == '__main__':
 #   app.run()

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




