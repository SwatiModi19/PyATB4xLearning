##multi level inheritance ---
# A -->B ---> C

class Grandfather:
    key = "2KG"

    def BHK1(self):
        print("1bhk")


class father(Grandfather):
    key = "22caret"

    def BHK2(self):
        print("2bhk")


class son(father):
    btc = "1BTC"

    def BHK3(self):
        print("3bhk")

s =son()
f=father()
g=Grandfather