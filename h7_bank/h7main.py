class Customer:
    last_id = 0
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id


    def __repr__(self):
        return 'Customer[{},{},{}]'.format(self.id, self.firstname, self.lastname)

class Account:
    last_id = 0
    def __init__(self, customer):
        Account.last_id += 1
        self.id = Account.last_id
        self.customer = customer
        self._balance = 0
        self.interest_rate = 0.13

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print('New deposit updated as: ' + str(self._balance))
        else:
            print('The amount is negative, we can not proceed, sorry. Your amount is:',amount, 'your balance is:', self._balance)

    def charge(self, amount):
        if amount > self._balance:
            raise NotEnoughBalanceException("You don't have enough Balance. Your Current Balance is " + str(self._balance)
                                            , self._balance)
        if amount <= 0:
            raise NegativeAmountException("The amount is negative. Please input the positive amount")
        else:
            self._balance -= amount
            print("Charge amount is: " + str(amount))
            print("New Balance updated as: " + str(self._balance))

    def get_balance(self):
        return self._balance

    def calc_interest(self, a=1):
        # a is number of growth periods in a year, default is 1
        return self._balance * (1 + self.interest_rate / a) ** a - self._balance

    def __repr__(self):
        return 'Account[{},{},{}]'.format(self.id, self.customer.lastname, self._balance)


class SavingsAccount(Account):
    interest_rate = 0.01
    def calc_interest(self):
        self._balance += self.interest_rate * self._balance

class CheckingAccount(Account):
    pass

class BankException(Exception):
    def __init__(self, msg, balance=None):
        super().__init__(msg)
        self.balance = balance

class NegativeAmountException(BankException):
    pass

class NotEnoughBalanceException(BankException):
    pass

class Bank:
    # Customer Factory
    def new_customer(self, first_name, last_name):
        # HOMEWORK: adding customer to a list
        c = Customer(first_name, last_name)
        self.customers.append(c)
        return c

    def new_account(self, customer):
        a = Account(customer)
        self.accounts.append(a)
        return a


    # Add account factory to bank
    def __init__(self):
        self.customers = []
        self.accounts = []
    #HOMEOWORK: Implementing transfer
    def transfer(self, amount, from_acc_id, to_acc_id):
        self.accounts[from_acc_id - 1].charge(amount)
        self.accounts[to_acc_id - 1].deposit(amount)
        if amount <= 0:
            raise NegativeAmountException("The amount is negative. Please input the positive amount")
        pass
    #list of customers and accounts
    def __repr__(self):
        return 'Bank(customers: {0}, account: {1})'.format(self.customers, self.accounts)


bank = Bank()
c1 = Customer('John', 'Smith')
#print(c1)
c2 = Customer('Anne', 'Brown')
#print(c2)
del c2
c2 = Customer('Anne2', 'Brown')
#print(c2)
a1 = bank.new_account(c1)
a2 = bank.new_account(c2)
#print(a1)
a1.deposit(2300)
a1.deposit(-100)
a1.charge(1000 )

#printing list of customers and accounts
print(bank)
#a2.deposit(-200)
print(a1.calc_interest())
#print(a1)
#print(a2)
try:
    a1.charge(400)
    a1.calc_interest()
    a1.charge(-200)
    print('After charging')
    print(a1)
except NotEnoughBalanceException as nebe:
     print('Exception: ' + str(nebe))
     print('Balance is {}'.format(nebe.balance))
#except BankException as nebe:
# except BankException as nebe:
 #    print('General Exception: ' + str(nebe))
 #except Exception as e:
 #     print(str(e))
except NegativeAmountException as nae:
     print('Exception: ' + str(nae))
print('running further')

a1.__balance = 500
print("A1_GET_BALANCE_debug_print",a1.get_balance())
print(a1.calc_interest())

#executing transfer #checking exceptions
a1.charge(-100)

bank.transfer(1, 2, -50)
