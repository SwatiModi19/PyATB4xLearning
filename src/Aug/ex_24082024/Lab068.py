## create a program to sum of 3 numbers from the input

num1= int(input("enter the number\n"))
num2= int(input("enter the number\n"))
num3= int(input("enter the number\n"))

def sum_of_3_numbers(n1,n2,n3):
    return n1+n2+n3

result= sum_of_3_numbers(num1,num2,num3)
print(result)
#or

result= sum_of_3_numbers(num1=10,num2=1,num3=7)
print(result)

