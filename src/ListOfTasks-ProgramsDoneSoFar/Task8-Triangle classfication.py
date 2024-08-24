# ### Task #8
#
# ✅ Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

a = float(input("enter the length of side1:\n"))
b = float(input("enter the length of side2:\n"))
c = float(input("enter the length of side3:\n"))

if a == b == c:
    print("The triangle is equilateral triangle")
elif a == b or b == c or c == a:
    print("The triangle is isosceles triangle")
else:
    print("The triangle is scalene triangle")
