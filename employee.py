class Employee:
    def __init__(self, name, address, branch):
        self.name = name
        self.address = address
        self.branch = branch
    
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
    

        