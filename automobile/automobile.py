#create an automobile class
#define a constructor
#constructor is a function tthat executes when an object is created

class Automobile():
    def __init__(self, make, model, vin, engine_size, owner, year):
        #Assign class properties values
        self.make = make
        self.model = model
        self.vin = vin
        self.engine_size = engine_size
        self.owner = owner
        self.year = year