###string

name = "Test"

print(name.upper())
print(name.lower())
print(len(name))

name2 = None   # null concept is not available in python
#name3 ="This is test" +1  #can only concatenate str (not "int") to str
name4 ="This is test" + "1"
name5 = "This is test" + str(1)
print(type(name2))
# print(type(name3))
print(type(name4))
print(name4)
print(type(name5))
print(name5)

age=10
age2 =10

## if value of the variables aew same then id value will be same (same location it will point )
## else it will be different


print (id(age))  #12345
print (id(age2))
