#create an automobile class
#define a constructor
#constructor is a function tthat executes when an object is created
import datetime

class Automobile():
    def __init__(self, make, model, vin, engine_size, owner, year):
        #Assign class properties values
        self.__make = make
        self.__model = model
        self.__vin = vin
        self.__engine_size = engine_size
        self.__owner = owner
        self.__year = year

    #create get and set methods for class properties

    #Create a method to print Automobile Information
    def print_info(self):
        print(f"{self.__year} {self.__make} {self.__model}")
        print(f"VIN: {self.__vin}, Engine size {self.__engine_size} ")
        print(f"Owner:  {self.__owner}\n")
    
    def get_age(self):
        current_date = datetime.datetime.now()
        this_year = current_date.year
        return this_year - self.__year

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_vin(self):
        return self.__vin
    
    def get_engine_size(self):
        return self.__engine_size
    

    def set_engine_size(self, new_size):
        self.__engine_size = new_size

    def get_owner(self):
        return self.__owner
    
    def set_owner(self, new_owner):
        self.__owner = new_owner

    def get_year(self):
        return self.__year