from my_services import app
from flask import request, jsonify
from neo4j import graph

@app.route('/rent-car', methods=['POST'])
def rent_car():
    data = request.get_json()
    customer_id = data.get('customer_id')
    car_id = data.get('car_id')

    # Check if the customer has a booking for the car
    query = f"MATCH (c:Customer)-[:BOOKED]->(car:Car) WHERE c.customer_id = {customer_id} AND car.car_id = {car_id} SET car.status = 'rented'"
    graph.run(query)

    return jsonify({'message': 'Car rented successfully'})


@app.route('/return-car', methods=['POST'])
def return_car():
    data = request.get_json()
    customer_id = data.get('customer_id')
    car_id = data.get('car_id')
    car_status = data.get('car_status')  # 'ok' or 'damaged'

    # Check if the customer has rented the car
    query = f"MATCH (c:Customer)-[:RENTED]->(car:Car) WHERE c.customer_id = {customer_id} AND car.car_id = {car_id} SET car.status = '{car_status}'"
    graph.run(query)

    return jsonify({'message': f'Car returned and marked as {car_status}'})


@app.route('/cancel-order-car', methods=['POST'])
def cancel_order_car():
    data = request.get_json()
    customer_id = data.get('customer_id')
    car_id = data.get('car_id')

    # Check if the customer has booked the car
    query = f"MATCH (c:Customer)-[:BOOKED]->(car:Car) WHERE c.customer_id = {customer_id} AND car.car_id = {car_id} SET car.status = 'available'"
    graph.run(query)

    return jsonify({'message': 'Car booking canceled successfully'})