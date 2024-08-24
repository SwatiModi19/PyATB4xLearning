# ### Task #4
#  Write a Python program to calculate the area of a circle given its
#  radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)

r = float(input("Enter the radius\n"))
pi = 3.14
area = pi * (r ** 2)
print(f"area of the circle with radius {r} is {area :.2f} square units")
