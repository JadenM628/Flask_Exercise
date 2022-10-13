from curses.ascii import isalpha
from datetime import date
from urllib import request
from flask import Flask, Response, render_template, request
import datetime

app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.


@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    currentDate = datetime.datetime.now()
    return render_template('index.html', currentDate=currentDate)


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    form = ''' 
            <div class="col-2">
                <h1>Home</h1>
                <h3>Enter an interger value:</h3>
                <form action="calculate" method="post">
                    <label for="number">Enter Number: </label>
                    <input type="text" id="number" name="number" placeholder="Enter a number.">
                    <button type="submit">Submit</button>
                </form>
            </div>  
    '''
    return Response(form)


@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    num = request.form.get("number")
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    if not num:
        return 'No Number Provided.<br><a href="/">Back to home</a>'
    elif num.isalpha():
        return f'{num} is not a integer!<br><a href="/">Back to home</a>'
    
    if int(num) % 2 == 0:
        return f'{num} is even.<br><a href="/">Back to home</a>'
    else:
        return f'{num} is odd.<br><a href="/">Back to home</a>'
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['number']
    # Write your to code here to check whether number is even or odd and render result.html page
    

@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    form = '''
            <div class="col-2">
                <h1>Register</h1>
                <h3>Enter Student Information below</h3>
                <form action="addStudentOrganisation" method="post">
                    <label for="name">Enter name: </label>
                    <input type="text" id="name">
                    <label for="orgs">Enter organisation: </label>
                    <select name="orgs" id="orgs">
                        <option value ="lazers">Charlotte Lazers</option>
                        <option value ="code9">Code 9</option>
                        <option value ="blazers">Wilmington Blazers</option>
                        <option value ="errors">Austin Errors</option>
                    </select>
                    <input type="submit" value="Register">
                </form>
    '''
    return Response(form)

@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    studentOrg = request.form['orgs']
    # Append this value to studentOrganisationDetails
    
    # Display studentDetails.html with all students and organisations
    return render_template('StudentDetails.html')