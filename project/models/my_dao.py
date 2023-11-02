from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import json

URI = 'neo4j+s://df132ca1.databases.neo4j.io'
AUTH =('neo4j', 'Cjwjw4-IB4plLSQIP648TceZuGI9ObbWiUkRbZ8YnRw')

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties

def findAllCars():
    with _get_connection().session() as session:
        cars = session.run("MATCH(a:Car)RETURN a;")
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json
    
def findCarByReg(reg):
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Car) where a.reg=$reg RETURN a;", reg=reg)
        print(cars)
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json
    
def save_car(make, model, reg, year, capacity, id, status):
    cars = _get_connection().execute_query(
        "MERGE (a:Car{make: $make, model: $model, reg: $reg, year: $year, capacity:$capacity, id:$id, status:$status}) RETURN a;",
        make=make, model=model, reg=reg, year=year,capacity=capacity, id=id, status=status)
    nodes_json = [node_to_json(record["a"]) for record in cars]
    print(nodes_json)
    return nodes_json

def update_car(make, model, reg, year, capacity, id, status):
    with _get_connection().session() as session:
        cars = session.run(
            "MATCH (a:Car{reg:$reg}) set a.make=$make, a.model=$model, a.year = $year, a.capacity = $capacity, a.id = $id, a.status = $status RETURN a;",
            reg=reg, make=make, model=model, year=year, capacity=capacity)
        print(cars)
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json
    
def delete_car(reg):
    _get_connection().execute_query("MATCH (a:Car{reg: $reg}) delete a;", reg=reg)

save_car("Volvo", "v90", "D1234", 2022, 5, 4, "available")
save_car("Aston Martin", "DB9", "A1234", 2011, 5, 1, "available")
save_car("Ford", "Explorer", "B1234", 2012, 7, 2, "available")
save_car("Ford", "Focus", "C1234", 2009, 5, 3, "available")