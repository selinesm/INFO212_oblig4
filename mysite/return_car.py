from project import app, graph
from flask import request, jsonify

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

if __name__ == '__main__':
    app.run(debug=True)
