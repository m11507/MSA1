class Student():
    def __init__(self, first_name, last_name, major, credit_hours, gpa, student_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__student_id = student_id
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_major(self):
        return self.__major
    
    def get_credit_hours(self):
        return self.__credit_hours
    
    def get_gpa(self):
        return self.__gpa
    
    def get_student_id(self):
        return self.__student_id
    
    def set_first_name(self, first):
        self.__first_name = first
    
    def set_last_name(self, last):
        self.__last_name = last

    def set_major(self, maj):
        self.__major = maj
    
    def set_credit_hours(self, cred):
        self.__credit_hours = cred

    def set_gpa(self, new_gpa):
        self.__gpa - new_gpa




    def get_class_level(self):
        if (int(self.__credit_hours) <= 30):
            return "Freshman"
        elif (int(self.__credit_hours) <= 60):
            return "Sophomore"
        elif (int(self.__credit_hours) <= 90):
            return "Junior"
        else:
            return "Senior"
    
    def update_credit_hours(self, additional_hours):
        if (additional_hours > 0):
            try:
                self.__credit_hours += additional_hours
            except:
                print("Error: Additional hours must be a positive number!")
        else:
            print("Error: additional hours must be a positive number!")

    def print_student_data(self):
        print(f"First name: {self.__first_name}")
        print(f"Last name: {self.__last_name}")
        print(f"Class: {self.get_class_level()}")
        print(f"Major: {self.__major}")
        print(f"Credit Hours: {self.__credit_hours}")
        print(f"GPA: {self.__gpa}")
        print(f"Student ID: {self.__student_id}")