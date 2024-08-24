# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}


num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))

# max
print("this is max  " , max(num1,num2))

# pow num1 to num2

print(pow(num1,num2))


# sub, mul, sum, div.
# num1 = int(input("Enter num1"))
# num2 = int(input("Enter num2"))

print(f"{"sum is:  "} {num1 + num2}")
print(f"{"sub is:  "} {num1 - num2}")
print(f"{"mul is:  "} {num1 * num2}")
print(f"{"div is:  "} {(num1 / num2):.4f}")  #### this will always in float


