
# Turn this diagram into code

class Customers():
    def __init__(self, CreateCompany, CreatePerson, DeleteCompany, DeletePerson):
        self.CreateCompany = CreateCompany
        self.CreatePerson = CreatePerson
        self.DeleteCompany = DeleteCompany
        self.DeletePerson =DeletePerson

class Customer():
    def __init__(self, address, phone):
        self.address = address
        self.phone = phone

class UpdateCustomer(Customer):
    pass

class Orders():
    def __init__(self, Create, Cancel):
        self.Create = Create
        self.Cancel = Cancel

class Order():
    def __init__(self, date, status):
        self.date = date
        self.status = status

class item():
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

class UpdateItem(item):
    pass

class Products():
    def __init__(self, Create, Delete, Update, SelctBelowThreshold):
        self.Create = Create
        self.Delete = Delete
        self.Update = Update
        self.SelctBelowThreshold = SelctBelowThreshold

class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Company(Customer):
    def info(self, name, regno):
        self.name = name
        self.regno = regno

class Person(Customer):
    def infoP(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname




