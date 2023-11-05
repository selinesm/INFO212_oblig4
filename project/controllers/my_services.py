
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, Flask
from project.models.my_dao import *
from project.models.User import *
from neo4j import GraphDatabase
from project import app


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
        record['year'], record['capacity'], record['id'], record['status'], record)

# The method uses the registration number to find the car
# object from database and removes the records
@app.route('/delete_car', methods=['DELETE'])
def delete_car_info():
    record = json.loads(request.data)
    print(record)
    delete_car(record['reg'])
    return findAllCars()




