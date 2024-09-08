class person:
        #class variable / instance variables
        #name = "Amit"  # hard coded value , to make it dynamic need to create a constructor

        def __init__(self,name):   ## parameterised constructor , it is used to  define the value of
                                    # the instance variable while object creation
                                    
            self.name = name

        def walk(self):
            self.name = name
            print(self.name)

amit = person("amit")
promod = person("promod")

print (amit.name)
print (promod.name)