###Enpasulation : u can bind the data variables n methods
### hide the data members ( class /variables /instance variables)
## by using only the members
''
class car:
    name = None
    pwd = 1234

    def __init__(self):
        print("DC")


    def change_pwd(self):
        self.pwd = "Test"
        print (self.pwd)

    def change_pwd2(self):
        self.pwd = "Test2"
        print(self.pwd)

ocar = car()
ocar.change_pwd()
ocar.change_pwd2()