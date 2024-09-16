
class son:
    gold = "2KG"

    def BHK1(self):
        print("1bhk")


class father(son):
    diamond = "22caret"

    def BHK2(self):
        print("2bhk")


class Grandfather(father):
    btc = "1BTC"

    def BHK3(self):
        print("3bhk")

s =son()
f=father()
g=Grandfather()