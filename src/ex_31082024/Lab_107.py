class person:  ### Blueprint

    ## Attibutes :
        id =None
        name =None
        age =None
        email =None
        height =None
        gender =None
        phone_no =None

    ## Behaviour
        # no args no return type
        def talk(self): ### NRNG--> Self --> "This" in Java , Self will be the first argument in every behaviour
            print("i can talk")

        def walk(self):
            print("i am walking")

            # No Arg with return type
        def walk_return(self):
            return "i am walking"

        ## Arg with no return type
        def sleep(self ,name):
            print("i am a method!!")
            print("sleep" ,name)

        ## Arg with return type
        def sleep2(self ,name):
            print("i am a method!!")
            print("sleep" , name)
            return None


## create an object of a class
##ObjectRef = ClassName() --> Object


Ram = person()  ## Ram is an object
Ram.name = "Ram"
print(Ram.name)
ram.talk()

sita = person()  ## sita is an object
sita.name = "sita"
print(sita.name)
sita.talk()