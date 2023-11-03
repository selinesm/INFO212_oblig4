from project import app
from flask import request, jsonify
from neo4j import graph
from project.models.my_dao import _get_connection
from project.controllers.customer import *
from project.models.my_dao import *
from project.models.Customer import *

"""
Customer:
    ordered_car = True/False
        - True: customer have a placed car order
        - False: customer have no car order

    reg = False/reg-number
        - False: no car is booked
        reg: car is booked and stores the ars reg-number

Car:
    status = "available" / "booked" / "rented"
        - available: car is available for ordering
        - booked: car is booked and not available
        - rented: car is rented by customer 
"""


# -------------------
    # Order Car
# -------------------
@app.route("/order_car", methods=["POST"])
def rent_car():
    record = json.loads(request.data)
    print(record)

    # find status of car
    temp = findCarByReg(record["reg"])
    car_status = temp[0]["status"]
    print(car_status)
    
    # find status of customer
    temp = findCustomerById(record["id"])
    customer_status = temp[0]["ordered_car"]

    if car_status == "available" and customer_status == False:

        with _get_connection().session() as session:
            car = session.run(
                "MATCH (a:Car{reg:$reg}) set a.status=$status RETURN a;",
                reg=record["reg"], status="booked"
            )
            customer = session.run(
                "MATCH (a:Customer{id:$id}) set a.ordered_car=$ordered_car, a.reg=$reg RETURN a;",
                id=record["id"], ordered_car=True, reg=record["reg"]
            )
            nodes_json_car = [node_to_json(record["a"]) for record in car]
            print(nodes_json_car)
            nodes_json_customer = [node_to_json(record["a"]) for record in customer]
            print(nodes_json_customer)
            return [nodes_json_car, nodes_json_customer]


# -------------------
    # Rent Car
# -------------------
@app.route("/rent_car", methods=["POST"])
def rent_car():
    record = json.loads(request.data)
    print(record)

    # find status of car
    temp = findCarByReg(record["reg"])
    car_status = temp[0]["status"]
    print(car_status)
    
    # find status of customer
    temp = findCustomerById(record["id"])
    customer_status = temp[0]["ordered_car"]
    customer_car_reg = temp[0]["reg"]

    if car_status == "booked" and customer_status == False and customer_car_reg == record["reg"]:

        with _get_connection().session() as session:
            car = session.run(
                "MATCH (a:Car{reg:$reg}) set a.status=$status RETURN a;",
                reg=record["reg"], status="booked"
            )
            customer = session.run(
                "MATCH (a:Customer{id:$id}) set a.ordered_car=$ordered_car, a.reg=$reg RETURN a;",
                id=record["id"], ordered_car=True, reg=record["reg"]
            )
            nodes_json_car = [node_to_json(record["a"]) for record in car]
            print(nodes_json_car)
            nodes_json_customer = [node_to_json(record["a"]) for record in customer]
            print(nodes_json_customer)
            return [nodes_json_car, nodes_json_customer]


# -------------------
    # Return Car
# -------------------
@app.route("/return_car", methods=["POST"])
def return_car():
    record = json.loads(request.data)
    print(record)

    # Finn statusen til bilen og kunden
    temp = findCarByReg(record["reg"])
    car_status = temp[0]["status"]
    print(car_status)

    temp = findCustomerById(record["id"])
    customer_status = temp[0]["rented_car"]

    if car_status == "rented" and customer_status == True:
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
                "MATCH (a:Customer{id:$id}) set a.ordered_car=$ordered_car, reg=$reg RETURN a;",
                id=record["id"], ordered_car=False, reg=False
            )
            nodes_json_car = [node_to_json(record["a"]) for record in car]
            print(nodes_json_car)
            nodes_json_customer = [node_to_json(record["a"]) for record in customer]
            print(nodes_json_customer)
            return [nodes_json_car, nodes_json_customer]



# -------------------
    # Cancel Order Car
# -------------------
@app.route('/cancel-order-car', methods=['POST'])
def cancel_order_car():
    record = json.loads(request.data)
    print(record)

    # find status of car
    temp = findCarByReg(record["reg"])
    car_status = temp[0]["status"]
    print(car_status)
    
    # find status of customer
    customer_status = findCustomerById(record["id"])
    customer_status = customer_status[0]["ordered_car"]

    if car_status == "booked" and customer_status == True:

        with _get_connection().session() as session:
            car = session.run(
                "MATCH (a:Car{reg:$reg}) set a.status=$status RETURN a;",
                reg=record["reg"], status="available"
            )
            customer = session.run(
                "MATCH (a:Customer{id:$id}) set a.ordered_car=$ordered_car, a.reg=$reg RETURN a;",
                id=record["id"], ordered_car=False, reg=False
            )
            nodes_json_car = [node_to_json(record["a"]) for record in car]
            print(nodes_json_car)
            nodes_json_customer = [node_to_json(record["a"]) for record in customer]
            print(nodes_json_customer)
            return [nodes_json_car, nodes_json_customer]