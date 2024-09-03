### Constructors --> its a special function in class , this is use to initialise
###  NAme of construction  --> __init__
### It will automaticaaly be called when an object is created


class dog():

    #A
    name = None

    # constructor  has no return type
    # def __init__(self):
    #     print("DC| it will be called automatically when an object is created")

    # def __init__(self,name):
    #     print("Called , Object is created")
    #     self.name = name

    def __init__(self, name ,age):
        print("Called , Object is created")
        self.name = name
        self.age = age

    #B
    def sleep(self):
        print("i can sleep")
        print ("who is sleeping "  + self.name , self.age)


# Dog1 = dog()   ### On running --> __init__ will automaticaaly be called  -> this is example of default constructor with no arguments
#print(Dog1.name) ## None

# Dog2 = dog("chow")   ### On running --> __init__ will automaticaaly be called with arguments
# print(Dog2.name)
#
# Dog3 = dog("Mow")
# print(Dog3.name)

Dog4 = dog("Mow" , 10)
print(Dog4.name)
print(Dog4.age)
Dog4.sleep()

