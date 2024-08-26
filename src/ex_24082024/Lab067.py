## User DEfined -- types of user defined
# 1.The can return somthing
# 2. they can not return --> no return type
# 3. They have parameters
# 4. They dont have parametrs or arguments


# 1st they can not return --> no return type
def greet():
    print("hi")

# 2.  No return type wuth  parameters

def greet_by_name(name):
    print("hi" , name)

# 3.  No return type wuth default  parameters --> this is not available in Java

def say_hello_default_arg(name="Test"):
    print("hi" , name)
say_hello_default_arg("Amit")
say_hello_default_arg(name="Swati")  ##positional argumaments
say_hello_default_arg()


def multiple_arg(name1,name2,name3):
    print("multiple arguments" , name1,name2,name3)

multiple_arg("Amit","swati","lakshya")
multiple_arg("Amit","swati","lakshya")



def multiple_arg(name1="Test1",name2="TEst2",name3="Test3"):
    print("multiple arguments" , name1,name2,name3)

multiple_arg("Amit","swati","lakshya")
multiple_arg("Amit","lakshya")



#4 . Argument and return type

#sum of 2 number
def sum_of_2_num(num1,num2):
    return num1+num2

# result = sum_of_2_num(10,25)
result = sum_of_2_num(10,25)