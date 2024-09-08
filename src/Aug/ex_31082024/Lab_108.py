## Note file name which is Lab_108.py need not required to be same as class name as we have in java.
# # in python the file name can be anything

class Dog:

    # A
        name =None
        breed =None
        color =None

       #B
        def sleep(self):
           print ("i can sleep")

        def bark(self):
           print ("i can bark")

        def food(self,food):
            print("I can eat" , food)

## create object of a class

Dog1 =Dog()
print (Dog1.name)
Dog1.name = "Chow"
print (Dog1.name)
Dog1.sleep()
print ("-------------------------------")

Dog2 = Dog()
print(Dog2.name)
Dog2.name = "Mow"
print(Dog2.name)

Dog3 = Dog1  ## ===> this to duplicate the objects
