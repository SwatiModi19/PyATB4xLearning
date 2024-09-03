# multiple arguments
def make_pizza(*topping,base)
    print(topping,base)

amit = make_pizza(*topping: "mushroom","onion",base="thin crust")


### def make_pizza(*topping,*base) ===>  this is not possible both argument cano not accept multiple input

