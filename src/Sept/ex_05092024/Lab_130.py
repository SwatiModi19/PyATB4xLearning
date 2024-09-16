##multi level inheritance ---
# A -->B ---> C

class Grandparent:
    key_gold = "2KG"

    def grandparent_method(self):
        return "grandparent's method"


class parent(Grandparent):

    def parent_method(self):
        return "parent's method"


class child(parent):
    btc = "1BTC"

    def child_method(self):
        return "child method"

child =child()
print(child.grandparent_method())