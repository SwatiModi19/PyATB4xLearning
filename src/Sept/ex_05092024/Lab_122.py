  ##Enpasulation

  class Myclass:
      #public variable (instance variable)
    public_var = "I am public"
    balance = 0
    #private variable

    __private_var = "I am private"
    __password = "12434"


    #protected variables
      _protected = "I am protected"



object = Myclass()
print(object.public_var)
print(object._protected)
print(object.balance)
print(object._protected)
print(object.__private_var)      # not possible to access private vriable outsid class

