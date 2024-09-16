### hierarical  inheritance

class father:

    def BHK1(self):
        return "Father 1BHK"

class son1(father):

    def BHK2(self):
        return "son1 2BHK"

class son2(father):

    def BHK3(self):
        return "son2 3BHK"

class son3(father):

    def Nohouse(self):
        return "son3 No house"


s=son1()
print(s.BHK1())
print(s.BHK2())
# print(s.BHK3())
