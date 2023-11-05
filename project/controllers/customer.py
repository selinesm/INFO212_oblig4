
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, Flask
from project.models.customer import *
from project.models.User import *
from neo4j import GraphDatabase
from project import app


@app.route("/get_customers", methods=["GET"])
def query_customers():
    return findAllCustomers()


@app.route('/get_customer_by_id', methods=['POST'])
def find_customer_by_id():
    try:
        record = request.get_json()  # Parse JSON data from the request body
        print(record)
        print(record['id'])
        return jsonify(findCustomerById(record['id']))
    except Exception as e:
        return jsonify({"error": "Invalid JSON data or missing 'id' field"}), 400


@app.route('/save_customer', methods=["POST"])
def save_customer_info():
    record = json.loads(request.data)
    print(record)
    return save_customer(
        record['name'], record['age'], record['address'], record['ordered_car'], record["reg"], record["id"], record["rented_car"])

@app.route('/update_customer', methods=['PUT'])
def update_customer_info():
    record = json.loads(request.data)
    print(record)
    return update_customer(
        record['name'], record['age'], record['address'], record['ordered_car'], record["reg"], record["id"], record["rented_car"])


@app.route('/delete_customer', methods=['DELETE'])
def delete_customer_info():
    record = json.loads(request.data)
    print(record)
    delete_customer(record['id'])
    return findAllCustomers()