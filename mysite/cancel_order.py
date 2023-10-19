from project import app, graph
from flask import request, jsonify

@app.route('/cancel-order-car', methods=['POST'])
def cancel_order_car():
    data = request.get_json()
    customer_id = data.get('customer_id')
    car_id = data.get('car_id')

    # Check if the customer has booked the car
    query = f"MATCH (c:Customer)-[:BOOKED]->(car:Car) WHERE c.customer_id = {customer_id} AND car.car_id = {car_id} SET car.status = 'available'"
    graph.run(query)

    return jsonify({'message': 'Car booking canceled successfully'})
