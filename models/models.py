# CARS
class Cars:
    def __init__(self, id, brand, model, year, location, status):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.location = location
        self.status = status


# CUSTOMER
class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


# EMPLOYEE
class Employee:
    def __init__(self, name, address, branch):
        self.name = name
        self.address = address
        self.branch = branch
