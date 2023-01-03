
# Turn this diagram into code

class Customers():
    def CreateCompany(self):
        pass

    def CreatePerson(self):
        pass

    def DeleteCompany(self):
        pass

    def DeletePerson(self):
        pass

class Customer():
    def __init__(self, address, phone):
        self.address = address
        self.phone = phone

    def update(self):
        pass

class Company(Customer):
    def __init__(self, name, regno):
        Customer.__init__(self, name, regno)

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




