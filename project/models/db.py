from models import Customer, Employee, Cars
from neo4j import GraphDatabase

customers = [
    {
        "name": "John",
        "age": 30,
        "address": "Bergen 123"
    }

]

employees = [
    {
        "name": "Bjørn Sander",
        "age": 40,
        "address": "Bilveien 123"
    }
]
print("""

<<<<<<< HEAD




""")
save_car("Volvo", "v90", "D1234", 2022, 5, 4, "available")
save_car("Aston Martin", "DB9", "A1234", 2011, 5, 1, "available")
save_car("Ford", "Explorer", "B1234", 2012, 7, 2, "available")
save_car("Ford", "Focus", "C1234", 2009, 5, 3, "available")

print("""





""")
=======
cars = [
    {
        "id": 1,
        "brand": "Ford",
        "model": "Explorer",
        "year": "2012",
        "location": "Bergen",
        "status": "Available"
    }
]
>>>>>>> 12361e7377df319c4b00445a3a3081e38c488a52

def connect():
    uri = "neo4j+s://df132ca1.databases.neo4j.io"
    username = "neo4j"
    password = "Cjwjw4-IB4plLSQIP648TceZuGI9ObbWiUkRbZ8YnRw"

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
        "MERGE (car:Car {id: $id}) "
        "ON CREATE SET car.brand = $brand, car.model = $model, car.year = $year, car.location = $location, car.status = $status"
    )
    tx.run(query, **car_data)

# Funksjon for å opprette en 'Customer' node i grafen
def create_customer_node(tx, customer_data):
    query = (
        "MERGE (customer:Customer {name: $name}) "
        "ON CREATE SET customer.age = $age, customer.address = $address"
    )
    tx.run(query, **customer_data)

# Funksjon for å opprette en 'Employee' node i grafen
def create_employee_node(tx, employee_data):
    query = (
        "MERGE (employee:Employee {name: $name}) "
        "ON CREATE SET employee.age = $age, employee.address = $address"
    )
    tx.run(query, **employee_data)

# Kall connect() for å koble til Neo4j og lagre data
connect()
