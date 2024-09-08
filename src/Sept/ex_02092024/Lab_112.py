## create a calculator class

class calc:

    def __init__(self ,a,b):   ###  parameterise  the constructor 
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b


    def sub(self):
        return self.a - self.b

    def mul(self):
         return self.a* self.b

    def div(self):
         return self.a/self.b

#create object

obj1 = calc(2,3)
obj2 = calc(2,3)
obj3 = calc(3,4)
obj4 = calc(10,2)

op = obj1.sum()
print (op)



