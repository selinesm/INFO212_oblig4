from project import app, graph
from flask import request, jsonify

@app.route('/rent-car', methods=['POST'])
def rent_car():
    data = request.get_json()
    customer_id = data.get('customer_id')
    car_id = data.get('car_id')

    # Check if the customer has a booking for the car
    query = f"MATCH (c:Customer)-[:BOOKED]->(car:Car) WHERE c.customer_id = {customer_id} AND car.car_id = {car_id} SET car.status = 'rented'"
    graph.run(query)

    return jsonify({'message': 'Car rented successfully'})
