## Conditions and loops
# write a program to take the user age and let him know  if he can go the club

# 21
# logic building
#
# take the inputs  --> int
# o/p --> string

# rough logic :
#  if age > 21 the print "go" else "can't go"


# step3  : write the logic

age = int(input("Enter the age \n"))

if age >= 21:
    print("can go to club as age is --> ", age)
else:
    print(f"cannot  go with this age is -->{age}")
