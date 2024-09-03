## pizza lovers

def make_pizza(*toppings):
    for i in toppings:
        print(i , end = " ; ")


a = make_pizza("tomato")
b= make_pizza("tomoto","onion","cheese")
c= make_pizza("tomoto","onion","cheese", "corn","jalpeno")


#Built *
r = max(1,2,3,4)
print (r)