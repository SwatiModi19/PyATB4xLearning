#### Encapsulation examples

class Bank:

    def __init__(self,account_number, balance):
        self.__account_number = account_number
        self.balance = balance
        self.__password = "25698"

    def deposit(self,amount):

        self.balance = self.balance + amount

    def check_balance(self):
        print(self.balance)

    def show_me_account_number(self,is_auth):    # / this is a public method
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not allowed")

    def __internal_method(self):   # / this is a private method
        print("private method")
        print(self.__account_number)
        print(self.balance)

Axis = Bank(9876543,100)
Axis.check_balance()
Axis.deposit(100)
Axis.check_balance()

# print(Axis.__account_number)   -> this is private in nature so we cannot call directly
Axis.show_me_account_number(False)
Axis.deposit(100)
Axis.check_balance()


# Axis.__internal_method()   # this is private in nature, hence not allowed to call outside class
