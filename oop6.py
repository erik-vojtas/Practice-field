class Customer:
    def __init__(self, name):
        self.name = name
        self.balance = 0

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = {}
        self.atms = []

    def buildATM(self, atm):
        newATM = Atm(self)
        self.atms.append(newATM)
        atm.setUpATM(self)

    def verifyCustomer(self, customer):
        customer_exist = False
        if self.customers != None:
            for k, v in self.customers.items():
                if customer == k:
                    customer_exist = True
        return customer_exist

    def setUpAccount(self, customer, deposit):
        if not self.verifyCustomer(customer):
            self.customers[customer] = deposit
            customer.balance += deposit
            return print(f'{customer.name} has set up a bank account in {self.name}')
        else:
            return print(f'{customer.name} has already a bank account in {self.name}.')

class Atm:
    def __init__(self, location):
        self.location = location
        self.banks = []

    def setUpATM(self, bank):
        self.banks.append(bank)

    def verifyCustomer(self, customer):
        isCustomer = False
        if self.banks != None:
            for b in self.banks:
                for k, v in b.customers.items():
                    if customer == k:
                        isCustomer = True
        return isCustomer

    def showBalance(self, customer):
        if self.verifyCustomer(customer):
            return customer.balance
        else:
            return print(f"{customer.name} doesn't have an access to a bank account.")


    def withDrawMoney(self, customer, amount):
        if self.verifyCustomer(customer):
            if customer.balance < amount:
                print(f'Not enough money on your account. Your balance is ${customer.balance}.')
            else:
                customer.balance = customer.balance - amount
                print(f'{customer.name} have withdrawn ${amount}, current balance is ${customer.balance}.')

    def depositCash(self, customer, deposit):
        if self.verifyCustomer(customer):
            if deposit > 0:
                customer.balance = customer.balance + deposit
                print(f'{customer.name} have deposited ${deposit}, current balance is ${customer.balance}.')




u1 = Customer("Marc")
u2 = Customer("John")
b1 = Bank("Bank Austria")
atm1 = Atm("Linz, Hauptplatz")

b1.buildATM(atm1)
b1.setUpAccount(u1, 1000)
b1.setUpAccount(u1, 5000)


atm1.withDrawMoney(u1, 900)
print(atm1.showBalance(u1))

atm1.depositCash(u1, 3000)
print(atm1.showBalance(u1))

atm1.showBalance(u1)
atm1.showBalance(u2)
