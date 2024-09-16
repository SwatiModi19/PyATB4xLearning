#### inheritance  -- aquarie the Attibutes and behavior from anothr class
###self is a default parameter / it represents the current object -> its used to access the instance variables

### single inheritance  A---> B

class Father():
    key= "2BHK"

    def car(self):
        print("Father car!! ALTO")
        print("Father car!! ALTO",self.key)

class son(Father):
    pass
    key2 ="3BHK"

    def home(self):
        print("3BHK")

    def truck(self):
        print("Truck")


father_obj = Father()
father_obj.car()

son_obj = son()
son_obj.car()