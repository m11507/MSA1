#import modules
from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#make a flask app
app = Flask(__name__)

app.config["DEBUG"] = True

#set a secret key to use when validating form data
app.config["SECRET_KEY"] = "password"

URL = "http://127.0.0.1:5000/api/students/all"

#function to request student data from the api
#input: url
#output: JSON student data
def get_student_data(url):
    #make a request
    response = requests.get(url)

    #convert format to json
    response_json = response.json()
    return response_json

#Function to return a list of unique majors
#input: url
#output: list of unique majors
def get_unique_majors(url):
    #url = "http://127.0.0.1:5000/api/students/all"
    #get a list of students from the student api
    student_list = get_student_data(url)

    #produce a list of unique majors
    unique_majors = []

    for student in student_list:
        if student["major"] not in unique_majors:
            unique_majors.append(student["major"])
    unique_majors.sort()
    return unique_majors



#create a route for the site index page that will display all student data
@app.route("/", methods=['GET'])
def index():
    #get the student data
    #make a request to the student data api url

    student_data = get_student_data(URL)

    return render_template('index.html', student_data = student_data)


    #send the student data to the index.html

@app.route('/majors', methods=['GET'])
def majors():
    #write code that gets a unique list of majors from student data
    major_list = get_unique_majors(URL)
    #get student data from the api: list of student dictionaries



    return render_template("majors.html", major_list=major_list)

@app.route('/majors', methods=['POST'])
def majors_post():
    major_list = get_unique_majors(URL)
    result_list = []
    #get the form data that was submitted
    major = request.form.get('major')
    #validate form data. If invalid form mdata, then show an error message
    #find students w/ selected major and return to the majors.html page
    if not major:
        flash("You must select a major")
    else:
        #find students with the selected major and return to the majors.html page
        url=URL
        student_list = get_student_data(url)
        #loop through list of students. If student major == major, place student in a result list
        for student in student_list:
            if student["major"] == major:
                result_list.append(student)
        #send the result list to the majors.html page
        

    return render_template('majors.html', major_list=major_list, result_list=result_list)

app.run(port=5005)