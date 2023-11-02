from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re

URI = 'neo4j+s://df132ca1.databases.neo4j.io'
AUTH =('neo4j', 'Cjwjw4-IB4plLSQIP648TceZuGI9ObbWiUkRbZ8YnRw')

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth= AUTH)
    driver.verify_connectivity()
    return driver

def findUserByUsername(username):
    data = _get_connection().execute_query('MATCH (a:User) where a.username = $username RETURN a;', username=username)
    if len(data[0])>0:
        user = User(username, data[0][0][0]['email'])
        return user
    
    else: 
        return None
    

class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email

    def get_Username(self):
        return self.username
    
    def set_Username(self,value):
        self.username = value

    def get_Email(self):
        return self.email
    
    def set_Email(self, value):
        self.email = value


def create_user(username, email):
    driver = GraphDatabase.driver(URI, auth=AUTH)

    with driver.session() as session:
        # Create a new user node in the database.
        session.write_transaction(_create_user, username, email)

def _create_user(tx, username, email):
    query = "CREATE (u:User {username: $username, email: $email})"
    tx.run(query, username=username, email=email)

# Example of creating a user
new_user = User("new_user", "new_user@example.com")
create_user(new_user.get_Username(), new_user.get_Email())

new_user1 = User("test", "test")
create_user(new_user1.get_Username(), new_user1.get_Email())