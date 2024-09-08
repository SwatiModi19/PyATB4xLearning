
#*args -- > multiple arguments with no limit --> its a list
def print_arguments(*args):   # minimum 1 argument is mandatory
    # print(args[0])
    for i in args:
        print(i,end=";")

print_arguments("amit","Lakshya","swati")
print_arguments("amit","Lakshya")
print_arguments("amit",10)
print_arguments("amit",10,True)
print_arguments("amit",10,True,False)
print_arguments("amit",10,True,False,"Test")

##

print("amit")
print("amit","Test")
print("amit","Test",True)
print("amit","Test",True,10)