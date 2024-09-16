### Single inheritance  example 2


class parent:

    gold = "2kg"

    def BHK2(self):
        print("2BHK")

class child(parent):
    diamond = "1kg"
    def BHK3(self):
        print("3BHK")


child_obj = child()
print(child_obj.gold)
child_obj.BHK2()
child_obj.BHK3()

parent_obj = parent()
parent_obj.BHK2()
# parent_obj.BHK3()  #AttributeError: 'parent' object has no attribute 'BHK3'. Did you mean: 'BHK2'?
# print(parent_obj.diamond)

