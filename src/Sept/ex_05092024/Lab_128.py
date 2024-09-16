## multiple inheritance
## A (Father)--> Child
## B(Mother)--> Child

class Father:
    key ="ABC"
    __pwd = "private"

    def __showpwd(self):
        print(self.__pwd)

    def father_money(self):
        return 5

    def father_home(self):
        return "This is from the father"

    def Home(self):
        return "This is from the father home same as mother"

class Mother:

    def mother_money(self):
        return 2

    def Home(self):
        return "This is from the mother"


class Son(Father ,Mother):    ##MRO -> method resolution order
    pass

s =Son()
print(s.father_home())
print(s.mother_money())
print(s.Home())

##there  is diamod issue with this  i.e. if same name methods are available in both parents i.e. father and mother both hold
#same funcion example Home
## if s.Home() ==> which home will be called
   # in Java this is not solved
   # in oython --> which ever is the first parent passed in argument
##MRO -> method resolution order    
# (son(Father ,Mother )  will be returned --> here Father will be returned
# (son(Mother,Father )  will be returned --> here Mother will be returned
