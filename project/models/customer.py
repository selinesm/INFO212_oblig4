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

def findAllCustomers():
    with _get_connection().session() as session:
        customers = session.run("MATCH(a:Customer)RETURN a;")
        nodes_json = [node_to_json(record["a"]) for record in customers]
        print(nodes_json)
        return nodes_json
    
def findCustomerById(id):
    with _get_connection().session() as session:
        customers = session.run("MATCH (a:Customer) where a.id=$id RETURN a;", id=id)
        print(customers)
        nodes_json = [node_to_json(record["a"]) for record in customers]
        print(nodes_json)
        return nodes_json
    
def save_customer(name, age, address, ordered_car, reg, id):
    customers = _get_connection().execute_query(
        "MERGE (a:Customer {id: $id}) "
        "SET a.name = $name, a.age = $age, a.address = $address, a.ordered_car = $ordered_car, a.reg=$reg, a.id = $id "
        "RETURN a;",
        name=name, age=age, address=address, ordered_car=ordered_car, reg=reg, id=id
    )
    node = get_node(customers)
    node_json = node_to_json(node)
    print(node_json)


def update_customer(name, age, address, ordered_car, reg, id):
    with _get_connection().session() as session:
        customers = _get_connection().execute_query(
        "MERGE (a:Customer {id: $id}) "
        "SET a.name = $name, a.age = $age, a.address = $address, a.ordered_car = $ordered_car, a.reg=$reg, a.id = $id"
        "RETURN a;",
        name=name, age=age, address=address, ordered_car=ordered_car, reg=reg, id=id
        )
        print(customers)
        nodes_json = [node_to_json(record["a"]) for record in customers]
        print(nodes_json)
        return nodes_json
    
def delete_customer(id):
    _get_connection().execute_query("MATCH (a:Customer{id: $id}) delete a;", id=id)

save_customer("Name", 30, "Heiåhå", False, False, 1)
save_customer("newName", 40, "NewAdress", False, False, 2)