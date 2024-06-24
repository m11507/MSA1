import student
from datetime import datetime


"""
Function to write error log file
input: error message
"""

def write_to_error_log(err_message):
    try:
        #open log file
        log_file = open("error_log.txt", "a")
        #write error message to log file
        log_file.write(f"{datetime.now()}: {err_message}\n")
        #close log file
        log_file.close()
    except Exception as err:
        print(err)
    return


def load_students(file_name):
    list_of_students = []
    student_file = open(file_name, "r")
    student_file.readline()
    counter = 1
    for line_of_data in student_file:
        counter += 1
        student_data = line_of_data.split(",")
        try:
            student1 = student.Student(student_data[0], student_data[1], student_data[2], student_data[3], student_data[4], student_data[5])
            list_of_students.append(student1)
        except:
            print(f"Error: The student's information is not complete at line {counter}.")
    
    return list_of_students









def main():
    array = load_students("students.csv")
    for student in array:
        student.print_student_data()





main()