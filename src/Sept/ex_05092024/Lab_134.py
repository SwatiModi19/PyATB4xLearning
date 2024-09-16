class gf:
    def car(self):
        return "old car"


class f(gf):
    def car(self):
        return "honda car"


class s(f):
    # def car(self):
    # return "New car"
    pass


son = s()
print(son.car())
