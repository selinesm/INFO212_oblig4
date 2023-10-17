# ------------------------------
# CARS
# ------------------------------
class Cars:
    def __init__(self, id, brand, model, year, location, status):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.location = location
        self.status = status

    @staticmethod
    def create(id, brand, model, year, location, status):
        # Create a new car object and return it
        return Cars(id, brand, model, year, location, status)

    def read(self):
        # Read and return information about the car
        return f"Car ID: {self.id}, Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Location: {self.location}, Status: {self.status}"

    def update(self, key, value):
        # Update a specific attribute of the car
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            return f"Attribute {key} does not exist in the car."

    @staticmethod
    def delete(car):
        # Delete a car object
        del car


# ------------------------------
# CUSTOMER
# ------------------------------
class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    @staticmethod
    def create(self, name, age, address):
        # create a new customer object
        return Customer(name, age, address)

    def read(self):
        # Read and return information about the customer
        return f"Name: {self.name}, age: {self.age}, address: {self.address}"

    def update(self, value, key):
        # Update a specific attribute of the car
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            return f"Attribute {key} does not exist in the car."

    @staticmethod
    def delete(customer):
        # delete a customer object
        del customer

# ------------------------------
# EMPLOYEE
# ------------------------------


