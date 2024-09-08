##Match statement this is same as switch statement in VB or java
## only availabel in python versions > 3.10

# syntax
# #match variable:
#     case pattern1:
#         # code block
#     case pattern2:
#         # code block

### write a program to ask user which browser he wants to run the automation

browser_name = (input("Enter the browser name \n"))
# print(browser_name.lower())
match browser_name.lower():

    case "crome":
        print("exicute the crome code")
    case "ie":
        print("exicute the ie code")
    case "firefox":
        print("exicute the ff code")
    case _:
        print ("Browser not found")