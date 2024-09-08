## how to take the user input and crete a class

## create a class and get input from user
class Person:

    def __init__(self):  # default constructor
        self.name = input("enter ur name\n")
        self.age = input("enter ur age\n")
        self.phone = input("enter ur phone\n")
        self.job = input("enter ur job\n")

    def Display_information(self):
        print(f"Name is : {self.name}")
        print(f"age is : {self.age}")
        print(f"phone is : {self.phone}")
        print(f"job is : {self.job}")

#create an object
Person1 =Person()

#call the fuction to display the information
Person1.Display_information()

