from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import json

URI = 'neo4j+s://df132ca1.databases.neo4j.io'
AUTH =('neo4j', 'Cjwjw4-IB4plLSQIP648TceZuGI9ObbWiUkRbZ8YnRw')

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

def get_node(data):
    return data[0][0][0]

def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties

def findAllEmployees():
    with _get_connection().session() as session:
        employees = session.run("MATCH(a:Employee)RETURN a;")
        nodes_json = [node_to_json(record["a"]) for record in employees]
        print(nodes_json)
        return nodes_json
    
def findEmployeeById(id):
    with _get_connection().session() as session:
        employees = session.run("MATCH (a:Employee) where a.id=$id RETURN a;", id=id)
        print(employees)
        nodes_json = [node_to_json(record["a"]) for record in employees]
        print(nodes_json)
        return nodes_json
    
def save_employee(name,address,branch, id):
    employees = _get_connection().execute_query(
        "MERGE (a:Employee {id: $id}) "
        "SET a.name = $name, a.address = $address, a.branch = $branch, a.id = $id "
        "RETURN a;",
        name=name,address=address,branch=branch, id=id
    )
    node = get_node(employees)
    node_json = node_to_json(node)
    print(node_json)


def update_employee(name,address, branch, id):
    with _get_connection().session() as session:
        employees = _get_connection().execute_query(
        "MERGE (a:Employee {id: $id}) "
        "SET a.name = $name, a.address = $address, a.branch = $branch, a.id = $id "
        "RETURN a;",
        name=name,address=address,branch=branch, id=id
        )
        print(employees)
        nodes_json = [node_to_json(record["a"]) for record in employees]
        print(nodes_json)
        return nodes_json
    
def delete_employee(id):
    _get_connection().execute_query("MATCH (a:Employee{id: $id}) delete a;", id=id)
