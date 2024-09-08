class car:

    def __init__(self , o_name , o_make ,o_model):
        self.o_name = o_name
        self.o_make = o_make
        self.o_model = o_model


    def start_engine(self):
        print( "starting a car with name" + self.o_name)
        print( "starting a car with make" + self.o_make)
        print( "starting a car with model" + self.o_model)

olambo = car("lambo","v2","1234")

olambo.start_engine()


oXuv = car("xuv","v2","2024")

oXuv.start_engine()