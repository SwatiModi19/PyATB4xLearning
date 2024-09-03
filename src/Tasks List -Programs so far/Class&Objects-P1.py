# Create a Employee Class
# A - name,age, phone, address, eid
# B - walk, talk, printdetails,
# with the Constructor which will set the values
# Ask the user about the information for E1, E2
# print the details of the E1, E2 via the print employee functions.

class Employee():
    #Attributes
        name = None
        age = None
        phone = None
        address = None
        eid = None

    ## Behaviour
        def walk(self , name):
            print("i can walk" , name)

        def talk(self):
            print ("I can talk")

     ## Constructor
        def __init__(self , name ,age , phone ,address,eid):
            self.name = name
            self.age = age
            self.phone = phone
            self.address = address
            self.eid = eid


E1 = input("enter the emp1\n")
E2 = input("enter the emp2\n")

Emp1 = Employee(E1,30,987654321,"Test123",1)
print (Emp1.name,Emp1.age,Emp1.phone,Emp1.address,Emp1.eid)
Emp1.walk(E1)
Emp1.talk()

Emp2 = Employee(E2,35,987655621,"Test456",2)
print (Emp2.name,Emp2.age,Emp2.phone,Emp2.address,Emp2.eid)
Emp2.walk(E2)
Emp2.talk()