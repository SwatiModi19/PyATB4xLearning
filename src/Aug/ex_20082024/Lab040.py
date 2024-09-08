# #Program to find the max between 3 numbers
#
# Step1 : user input -> float
# Step2 : o/p : int or string with max number
# Step3 : logic :

### if one condition then if condition: else
### if more condition then  if condition: elif condiotion: else:


num1 = float(input("enter num1: \n"))
num2 = float(input("enter num2: \n"))
num3 = float(input("enter num3: \n"))

if num1 > num2 and num1 > num3:
    print(f"{num1} is max")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is max")
else:
    print(f"{num3} is max")

maxnum = max(num1, num2, num3)
print (maxnum)
