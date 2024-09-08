## create a calculator class

class calc:

    def __init__(self):   ### default constructor - we are not using it
        print("DC")

    def sum(self ,a,b):
        return a+b


    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
         return a*b

    def div(self,a,b):
         return a/b

#create object

objRefernce = calc()

# a = input("enter the input a \n")
# b = input("enter the input b \n")

sunR = objRefernce.sum(2,4)
subR = objRefernce.sub(6,2)
mulR = objRefernce.mul(2,3)
divR = objRefernce.div(10,2)

print (f"{sunR} ,{subR},{mulR},{divR}", end = "\n")
