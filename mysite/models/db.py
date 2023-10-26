from models import Customer, Employee, Cars
from neo4j import GraphDatabase

customers = [
    {
        "name": "John",
        "age": 30,
        "address": "Bergen 123"
    },
]

employees = [
    {
        "name": "Bjørn Sander",
        "age": 40,
        "address": "Bilveien 123"
    }
]

cars = [
    {
        "id": 1,
        "brand": "Ford",
        "model": "Explorer",
        "year": "2012",
        "Location": "Bergen"
    }
]

def connect():

    uri = "bolt://localhost:7687"
    username = "neo4j"
    password = "password"

    driver = GraphDatabase.driver(uri, auth=(username, password))

    with driver.session() as session:
        # Opprett noder for kunder, ansatte og biler fra eksisterende data
        for customer_data in customers:
            create_customer_node(session, customer_data)
        
        for employee_data in employees:
            create_employee_node(session, employee_data)
        
        for car_data in cars:
            create_car_node(session, car_data)


    driver.close()

    # Funksjon for å opprette en 'Car' node i grafen
def create_car_node(tx, car_data):
    query = (
        "CREATE (car:Car {id: $id, brand: $brand, model: $model, year: $year, location: $location, status: $status})"
    )
    tx.run(query, **car_data)  # **car_data brukes for å pakke opp dataene fra dictionarien


# Funksjon for å opprette en 'Customer' node i grafen
def create_customer_node(tx, customer_data):
    query = (
        "CREATE (customer:Customer {name: $name, age: $age, address: $address})"
    )
    tx.run(query, **customer_data)  # **customer_data brukes for å pakke opp dataene fra dictionarien

# Funksjon for å opprette en 'Employee' node i grafen
def create_employee_node(tx, employee_data):
    query = (
        "CREATE (employee:Employee {name: $name, age: $age, address: $address})"
    )
    tx.run(query, **employee_data)  # **employee_data brukes for å pakke opp dataene fra dictionarien

# Kall connect() for å koble til Neo4j og lagre data
connect()