from project import app
from flask import request, jsonify
from neo4j import graph
from project.models.my_dao import _get_connection
from project.controllers.customer import *
from project.models.my_dao import *
from project.models.customer import *


@app.route("/rent_car", methods=["POST"])
def rent_car():
    record = json.loads(request.data)
    print(record)

    # find status of car
    car_status = findCarByReg(record["reg"])
    car_status = car_status[0]["status"]
    print(car_status)
    
    # find status of customer
    customer_status = findCustomerById(record["id"])
    customer_status = customer_status[0]["rented_car"]

    if car_status == "available" and customer_status == False:

        with _get_connection().session() as session:
            car = session.run(
                "MATCH (a:Car{reg:$reg}) set a.status=$status RETURN a;",
                reg=record["reg"], status="unavailable"
            )
            customer = session.run(
                "MATCH (a:Customer{id:$id}) set a.rented_car=$rented_car RETURN a;",
                id=record["id"], rented_car=True
            )
            nodes_json_car = [node_to_json(record["a"]) for record in car]
            print(nodes_json_car)
            nodes_json_customer = [node_to_json(record["a"]) for record in customer]
            print(nodes_json_customer)
            return [nodes_json_car, nodes_json_customer]



"""@app.route('/rent-car', methods=['POST'])
def rent_car():
    data = request.get_json()
    customer_id = data.get('customer_id')
    car_id = data.get('car_id')

    # Check if the customer has a booking for the car
    query = f"MATCH (c:Customer)-[:BOOKED]->(car:Car) WHERE c.customer_id = {customer_id} AND car.car_id = {car_id} SET car.status = 'rented'"
    graph.run(query)

    return jsonify({'message': 'Car rented successfully'})
"""

@app.route("/return_car", methods=["POST"])
def return_car():
    record = json.loads(request.data)
    print(record)

    # Finn statusen til bilen og kunden
    car_status = findCarByReg(record["reg"])
    car_status = car_status[0]["status"]
    print(car_status)

    customer_status = findCustomerById(record["id"])
    customer_status = customer_status[0]["rented_car"]

    if car_status == "unavailable" and customer_status == True:
        # Håndter tilfelle der kunden har leid bilen
        car_status = "available"
        if "car_status" in record:
            # Sjekk om det er en "car_status" -parameter i forespørselen for å oppdatere bilens tilstand
            car_status = record["car_status"]

        with _get_connection().session() as session:
            car = session.run(
                "MATCH (a:Car{reg:$reg}) set a.status=$status RETURN a;",
                reg=record["reg"], status=car_status
            )
            customer = session.run(
                "MATCH (a:Customer{id:$id}) set a.rented_car=$rented_car RETURN a;",
                id=record["id"], rented_car=False
            )
            nodes_json_car = [node_to_json(record["a"]) for record in car]
            print(nodes_json_car)
            nodes_json_customer = [node_to_json(record["a"]) for record in customer]
            print(nodes_json_customer)
            return [nodes_json_car, nodes_json_customer]



"""@app.route('/return-car', methods=['POST'])
def return_car():
    data = request.get_json()
    customer_id = data.get('customer_id')
    car_id = data.get('car_id')
    car_status = data.get('car_status')  # 'ok' or 'damaged'

    # Check if the customer has rented the car
    query = f"MATCH (c:Customer)-[:RENTED]->(car:Car) WHERE c.customer_id = {customer_id} AND car.car_id = {car_id} SET car.status = '{car_status}'"
    graph.run(query)

    return jsonify({'message': f'Car returned and marked as {car_status}'})"""


@app.route('/cancel-order-car', methods=['POST'])
def cancel_order_car():
    data = request.get_json()
    customer_id = data.get('customer_id')
    car_id = data.get('car_id')

    # Check if the customer has booked the car
    query = f"MATCH (c:Customer)-[:BOOKED]->(car:Car) WHERE c.customer_id = {customer_id} AND car.car_id = {car_id} SET car.status = 'available'"
    graph.run(query)

    return jsonify({'message': 'Car booking canceled successfully'})