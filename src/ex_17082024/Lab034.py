# Program to find the area of a circle
import math

##logic building formula

##Step1 : figure out the input
# inputs --> r --> data type --> float
# pi -->3.14
# power --> ** or pow  --> use any

# o/p --> float  - area, print area

##Step2: Write rough logic
## area = pi* (r**2)

# step3 -> write the logic

radius = float(input("Enter the radius of the circle: \n"))
print(radius)

area = math.pi * math.pow(radius, 2)
print("The area of the circle is-->" ,area)
print(f"The area of the circle is-->  {area: .2f}")
