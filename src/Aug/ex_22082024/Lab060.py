usertype =input("Enter the user type,admin,manager , guest \n")

match usertype.lower():

    case "admin"|"manager":
        print("Hello sir")
    case "guest":
        print("Hello guest")
    case _:
        print("hello there")