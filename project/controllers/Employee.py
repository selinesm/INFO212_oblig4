from flask import Blueprint, render_template, request, redirect, url_for, jsonify, Flask
from project.models.Employee import *
from project.models.User import *
from neo4j import GraphDatabase
from project import app


@app.route("/get_employees", methods=["GET"])
def query_employees():
    return findAllEmployees()


@app.route('/get_employee_by_id', methods=['POST'])
def find_employee_by_id():
    try:
        record = request.get_json()  # Parse JSON data from the request body
        print(record)
        print(record['id'])
        return jsonify(findEmployeeById(record['id']))
    except Exception as e:
        return jsonify({"error": "Invalid JSON data or missing 'id' field"}), 400


@app.route('/save_employee', methods=["POST"])
def save_employee_info():
    record = json.loads(request.data)
    print(record)
    return save_employee(
        record['name'], record['address'], record["branch"], record["id"])

@app.route('/update_employee', methods=['PUT'])
def update_employee_info():
    record = json.loads(request.data)
    print(record)
    return update_employee(
        record['name'], record['address'], record["branch"], record["id"])


@app.route('/delete_employee', methods=['DELETE'])
def delete_employee_info():
    record = json.loads(request.data)
    print(record)
    delete_employee(record['id'])
    return findAllEmployees()