from models import Employee

@staticmethod
def create(name, address, branch):
    return Employee(name, address, branch)
        
def read(self):
    return f"Name: {self.name}, address: {self.address}, branch: {self.branch}"

def update(self):
    pass

@staticmethod
def delete(employee):
    del employee
