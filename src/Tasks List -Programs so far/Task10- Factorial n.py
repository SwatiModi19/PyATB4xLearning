# Task #10 -
# ✅ Factorial n = 5 5! -->5*4*3*2*1 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24
# n= or 1 -> fact =1
# N 5 - > 5*4*3*2*1
##  factorial only works with integers
num = int(input("Enter the num : \n "))
fact = 1
if num == 0 or num == 1:
    fact = 1
    print(1)

else:

    for i in range(1, num + 1):
        fact = fact * i
print(fact)
