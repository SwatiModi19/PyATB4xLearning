a= 10  # global variable

class person:
    b=11    # instance variable - belongs to class

    def print_infor(self):
        a="hello"
        print(a)
        #print(self.b)
# create obj

obj1 = person()
a=5
#b=10
# print (self.b)    ## this is wrong as b is an instance variable belongs to class
op = obj1.print_infor()

print(op)